import os
from typing import List, Any, Optional
import uuid
from pinecone import Pinecone
import json
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone as langchain_pinecone
import os
import time
from langchain.embeddings import HuggingFaceEmbeddings

from models.models import Document as PsychicDocument, VectorStore, AppConfig
embeddings_model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
embed_model = HuggingFaceEmbeddings(model_name='all-mpnet-base-v2')
embeddings_dimension = 768

def find_highest_similarity(tuples_list):
    highest_value = None
    highest_index = None
    for index, tuple_item in enumerate(tuples_list):
        last_element = tuple_item[-1]
        if highest_value is None or last_element > highest_value:
            highest_value = last_element
            highest_index = index
    return highest_value, highest_index

import hashlib

def generate_key(question, freq):
    # Concatenate the question text and frequency
    key_string = f"{question}_{freq}"
    
    # Hash the concatenated string to generate a unique key
    key = hashlib.sha256(key_string.encode()).hexdigest()
    
    return key


class CacheVectorStore():
    def __init__(self, max_size=128, cache_file='data.json'):
        print(f"Initializing cache with size: {max_size}")
        self.max_size = max_size
        self.cache_file = cache_file
        self.load_cache()
        self.api_key = "475a65d3-ae34-4a91-91a7-2e0f6da62274"
        self.client = Pinecone(api_key=self.api_key)
        self.index_name = "test-cache"
        try:
            self.index = self.client.Index(self.index_name)
        except:
            existing_indexes = [index_info["name"] for index_info in self.client.list_indexes()]
            if self.index_name not in existing_indexes:
                self.create_index(
                    self.index_name,
                    dimension=1536,  # dimensionality of ada 002
                    metric='dotproduct',
                )
                while not self.describe_index(self.index_name).status['ready']:
                    time.sleep(1)
        self.index = self.client.Index(self.index_name)
        time.sleep(1)
        print(self.index.describe_index_stats())
        text_field = "text"
        self.vectorstore = langchain_pinecone(self.index, embed_model.embed_query, text_field)

    async def search_cache(self, query):
        docs_and_scores = self.vectorstore.similarity_search_with_score(query)
        print(docs_and_scores)
        best_sim, best_index = find_highest_similarity(docs_and_scores)
        print(best_sim)
        print("cache during search")
        print(self.cache)
        if best_sim is None or best_sim < 0.85:
            # query hasn't been asked before
            # q-a must be added to cache
            return None
        else:
            print("chunk id searched")
            
            ## UPDATE CACHE ENTRY

            # best_doc = docs_and_scores[best_index]
            # chunk_id = best_doc[0].metadata["chunk-id"]
            # print(chunk_id)
            # self.cache[chunk_id]["freq"] += 1
            # self.cache[chunk_id]["last_access_time"] = time.time()
            # # if len(self.cache) > self.max_size:
            # #     self.remove_least_recently_used()
            # await self.save_cache()
            return chunk_id, self.cache[chunk_id]["answer"]
        

    async def add(self, query: str, answer=None, chunk_id=None):
        print(self.cache)
        print(chunk_id)
        print(answer)
        if answer is not None:
            # first time addition
            question_embeddings = embeddings_model.encode(query)
            chunk_id = generate_key(query, 1)
            upsert_data = [{
                "id": str(chunk_id),
                "values": question_embeddings.tolist(),
                "metadata": {"chunk-id": chunk_id, "text": query}
            }]
            self.index.upsert(upsert_data)

            ## CREATE CACHE ENTRY
            
            # self.cache[chunk_id] = {"question": query, "answer": answer, "freq": 1, "last_access_time": time.time()}
            # if len(self.cache) > self.max_size:
            #     await self.remove_least_recently_used()
            # await self.save_cache()
            return "added"
        else:

            self.cache[chunk_id]["freq"] += 1
            self.cache[chunk_id]["last_access_time"] = time.time()
            if len(self.cache) > self.max_size:
                await self.remove_least_recently_used()
            start = time.time()
            await self.save_cache()
            end = time.time()
            print(end-start)
            return "Increased"
        

    async def get_frequent(self):
        print(self.cache)
        sorted_items = sorted(self.cache.values(), key=lambda x: x['freq'])
        if len(sorted_items) <= 5:
            top_5_questions = sorted_items
        else:
            top_5_questions = sorted_items[:5]
        return top_5_questions

    async def remove_least_recently_used(self):
        print(self.cache)
        oldest_query = min(self.cache, key=lambda x: self.cache[x].get('last_access_time', 0))
        del self.cache[oldest_query]
        id_to_delete = oldest_query
        self.index.delete(ids=[id_to_delete])
        print(self.index.describe_index_stats())

    def load_cache(self):
        if os.path.exists(self.cache_file):
            with open(self.cache_file, 'r') as f:
                self.cache = json.load(f)
        else:
            self.cache = {}
        print("loading cache.....")
        print(self.cache)

    async def save_cache(self):
        with open(self.cache_file, 'w') as f:
            json.dump(self.cache, f)

    async def clear_cache(self):
        # Delete all entries from the cache
        self.cache = {}
        # Save the empty cache
        await self.save_cache()
        # Delete all vectors from the Pinecone index
        all_ids = list(self.index.list())
        print(all_ids)
        if all_ids:
            self.index.delete(ids=all_ids)

        print(self.index.describe_index_stats())
        return "Cache cleared successfully."