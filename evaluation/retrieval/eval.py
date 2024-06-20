
import re
import numpy as np
from tqdm import tqdm
from utils import get_retriever

def load_golden_context(path):
    from pathlib import Path
    import json

    # ../datasets/eval_qst.json
    golden_dataset_path = Path(path)
    data = []
    # Read the JSON file
    with open(golden_dataset_path, 'r', encoding='utf-8') as json_file:
        # Load the JSON data into a list
        data = json.load(json_file)

    return data

def sanity_check_data(data):
    print("Data: ")
    print()
    print(data[:5])

def load_retriever(embedding_model_name):
    
    retriever = get_retriever(similarity_top_k=5, embedding_model_name=embedding_model_name)
    return retriever

def run_retrieval_evaluation(data, retriever):

    results = []
    
    for entry in tqdm(data):
        query = entry["question"]
        expected_source = entry['source']
        
        retrieved_nodes = retriever.retrieve(query)
        retrieved_sources = [node.metadata['chunk_id'] for node in retrieved_nodes]
        
        # If our label does not include a section, then any sections on the page should be considered a hit.
        if "#" not in expected_source:
            retrieved_sources = [source.split("#")[0] for source in retrieved_sources]
        
        if expected_source in retrieved_sources:
            is_hit = True
            score = retrieved_nodes[retrieved_sources.index(expected_source)].score
        else:
            is_hit = False
            score = 0.0
        
        result = {
            "is_hit": is_hit,
            "score": score,
            "retrieved": retrieved_sources,
            "expected": expected_source,
            "query": query,
        }
        results.append(result)

        return results
    
def sanity_check_results(results):
    print("Results: ")
    print()
    print(results[:2])

    
def get_hit_rate(results):
    return np.mean([r["is_hit"] for r in results])

def main():
    import nest_asyncio
    nest_asyncio.apply()

    data = load_golden_context("../datasets/golden_sources.json")
    sanity_check_data(data)
    retriever = load_retriever('sentence-transformers/all-mpnet-base-v2')
    results = run_retrieval_evaluation(data, retriever)
    sanity_check_results(results)
    hit_rate = get_hit_rate(results)
    print("Hit rate: "+ str(hit_rate))



if __name__ == "__main__":
    main()
