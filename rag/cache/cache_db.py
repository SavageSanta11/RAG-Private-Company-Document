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
from cache.db_interact import get_faqs, update_cache_entry, add_to_cache

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
    def __init__(self, max_size=128):
        print(f"Initializing cache with size: {max_size}")
        self.max_size = max_size
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
        if best_sim is None or best_sim < 0.85:
            # query hasn't been asked before
            # q-a must be added to cache
            return None
        else:
            best_doc = docs_and_scores[best_index]
            chunk_id = best_doc[0].metadata["chunk-id"]

            update_response = update_cache_entry(chunk_id, time.time())
            print(update_response)
            cached_response = update_response['cache_entry']["entry_info"]["answer"]
            if "message" not in cached_response:
                print("Cache entry updated succcessfully")
                return cached_response
            else:
                return "Model cache service is down. Please try again later."
        

    async def add_to_cache(self, query: str, answer=None, chunk_id=None):
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


            entry_info =  {"question": query, "answer": answer, "freq": 1, "last_access_time": time.time()}
            new_cache_obj = {
                "chunk_id": chunk_id,
                "entry_info": entry_info
            }
            cache_add_response = add_to_cache(new_cache_obj)
            if cache_add_response["size_limit_flag"] == True:
                ### an entry has been removed the mongo db so it has to be removed from pinecone too
                removed_chunk_id = cache_add_response["removed_chunk_id"]
                self.index.delete(ids=[removed_chunk_id])
            return "New cache entry created"
        

    async def get_frequent(self):
        faqs = get_faqs()
        return faqs

    