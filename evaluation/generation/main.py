import json

# Assuming your JSON file is named 'data.json'
file_path = '../datasets/responses_iter1_para.json'

# Open the file and load its contents
with open(file_path, 'r') as file:
    data = json.load(file)

rag_responses = []
human_responses = []
for i in range(0, 10):
    rag_responses.append(data[i]["rag_response"])
    human_responses.append(data[i]["human_response"])
    
predictions_dict = {
    "RAG Iteration 1": rag_responses,
}

from eval import generate_metrics_summary
result = generate_metrics_summary(human_responses, predictions_dict)

print(result["rouge"])

print(result["bleu"])

print(result["meteor"])

print(result['bert_score'])

print(result['bleurt_score'])