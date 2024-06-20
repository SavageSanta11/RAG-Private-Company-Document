import numpy as np
import os
from llama_index.embeddings import HuggingFaceEmbedding


EMBEDDING_DIMENSIONS = {
    'sentence-transformers/all-mpnet-base-v2': 768,
}

def get_embedding_model(model_name, embed_batch_size=100):
    return HuggingFaceEmbedding(
        model_name=model_name,
        embed_batch_size=embed_batch_size
    )
    