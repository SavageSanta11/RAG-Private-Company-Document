## evaluate responses (automated) 

import requests
import json
import time
with open('datasets/questions_human_response.json', 'r', encoding='utf-8') as file:
    questions_data = json.load(file)

responses = []

for question_data in questions_data:
    question = question_data["question"]
    human_response = question_data["human_response"]
    url = "http://localhost:8080/ask-question"
    payload = json.dumps({
        "question": question,
        "email": "jonah@gmail.com"
    })
    headers = {
        'Content-Type': 'application/json',
    }
    start = time.time()
    rag_response = requests.request("POST", url, headers=headers, data=payload)
    end = time.time()
    data = rag_response.json()
    
    responses.append({
        "question": question,
        "rag_response": data["answer"],
        "human_response": question_data["human_response"],
        "time_taken": end - start
    })

json_data = json.dumps(responses, indent=2)


with open('excelincluded_paragraph.json', 'w') as file:
    file.write(json_data)
