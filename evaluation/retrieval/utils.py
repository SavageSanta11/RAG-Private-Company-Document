from llama_index import VectorStoreIndex, ServiceContext
from llama_index.vector_stores import PineconeVectorStore
from data import get_embedding_model
import pinecone
    
def _get_vector_store_index(
    service_context,
    embedding_model_name,
):
    ### PLEASE PASTE YOUR OWN API KEY HERE
    api_key = ""
    pinecone.init(api_key=api_key, environment="gcp-starter")
    pinecone_index = pinecone.Index("langchain-retrieval-agent")
    vector_store = vector_store = PineconeVectorStore(
        pinecone_index=pinecone_index,
        add_sparse_vector=True,
    )
    index = VectorStoreIndex.from_vector_store(
        vector_store, 
        service_context=service_context
    )
    return index


def get_retriever(    
    embedding_model_name = "sentence-transformers/all-mpnet-base-v2",
    similarity_top_k=2
):

    embed_model = get_embedding_model(embedding_model_name)
    service_context = ServiceContext.from_defaults(embed_model=embed_model, llm=None)

    index = _get_vector_store_index(service_context, embedding_model_name)
    return index.as_retriever(similarity_top_k=similarity_top_k)


