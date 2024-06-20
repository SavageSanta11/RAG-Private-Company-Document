# import requests

# question = "What is the capital of the USA?"
# context = "USA is the United States of America"
# resp = requests.post(
#     # "https://model-7qrjr693.api.baseten.co/development/predict",
#     "https://model-5womggkq.api.baseten.co/production/predict",
#     headers={"Authorization": "Api-Key Z2VsJ74w.bQtNZvpg0BAsRjiBaQCPAYEfI8G92IY1"},
#     json={"prompt": "<s> [INST] You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise. [/INST] </s> [INST] Question: {question} Context: {context} Answer: [/INST]"},
# )

# print(resp.json())

# import requests
# import json

# url = "http://34.41.162.233:8080/ask-question"

# payload = json.dumps({
#   "question": "What is my annual leave entitlement if I joined the company on/after 1st May 2007?"
# })
# headers = {
#   'Content-Type': 'application/json'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)

import requests
import json

# url = "http://34.133.161.51:8080/jonah@gmail.com/add-message"

# dburl = "http://34.133.161.51:8080/"
# email = "jonah@gmail.com"
# sendurl = f"{dburl}{email}/add-message"
# userquery = "What costs do I need to bear if i damage my laptop"
# llmresponse = "If you damage your laptop as an employee of DB Schenker, the costs you need to bear are as follows:\n\n* For the first year of purchase: 60% of the original purchase price.\n* For the second year of purchase: 30% of the original purchase price.\n* For the third year of purchase: 15% of the original purchase price.\n\nAfter the third year of purchase, you will need to bear a flat rate of S$500 or 15% of the original purchase price, whichever is lower.\n\nIt's important to note that these costs apply only if you lose your laptop within the course of your employment. If you lose your laptop again, you will have to bear the full replacement cost.</s>"
# payload = json.dumps({
#  userquery : llmresponse
# })
# headers = {
#   'Content-Type': 'application/json'
# }

# response = requests.request("POST", sendurl, headers=headers, data=payload)

# print(response.text)

import requests

resp = requests.post(
    "https://model-03y6r8vq.api.baseten.co/production/predict",
    headers={"Authorization": "Api-Key yVi5nLbq.T0hirobLIBtEoQTmY1vFVJ57Jj2MNf1g"},
    json={'prompt': 'What is the meaning of life?'},
)

print(resp.json())