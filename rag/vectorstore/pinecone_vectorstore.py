import os
from typing import List, Any, Optional
import uuid
from pinecone import Pinecone

from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone as langchain_pinecone
import os
import time
from langchain.embeddings import HuggingFaceEmbeddings

from models.models import Document as PsychicDocument, VectorStore, AppConfig
embeddings_model = HuggingFaceEmbeddings(model_name= "all-mpnet-base-v2")
embeddings_dimension = 1536


class PineconeVectorStore():
    def __init__(self):
        api_key = None # replace with Pinecone API key
        self.client = Pinecone(api_key=api_key)
        # index_name = "capstone-embed-paragraphs-3"
        index_name = None # replace with Pinecone Index name
        try:
            self.index = self.client.Index(index_name)
        except:
            
            existing_indexes = [
                index_info["name"] for index_info in self.client.list_indexes()
            ]

            # check if index already exists (it shouldn't if this is first time)
            if index_name not in existing_indexes:
                # if does not exist, create index
                self.create_index(
                    index_name,
                    dimension=1536,  # dimensionality of ada 002
                    metric='dotproduct',
                )
                # wait for index to be initialized
                while not self.describe_index(index_name).status['ready']:
                    time.sleep(1)
        self.index = self.client.Index(index_name)
        time.sleep(1)
        print(self.index.describe_index_stats())
        text_field = "text"  # the metadata field that contains our text
        self.vectorstore = langchain_pinecone(
            self.index, embeddings_model.embed_query, text_field
        )


    async def query(self, query: str):
       
        results = self.vectorstore.similarity_search(
            query,  # our search query
            k=3  # return 3 most relevant docs
        )
        print(results)
        results = [
            PsychicDocument(
                id=str(doc.metadata["chunk-id"]),
                title=doc.metadata["doc-name"],
                content=doc.page_content,
            )
            for doc in results
        ]
        return results