db_url = None # replace with conversation history API URL

import requests
import json

def send_message_to_conversation_db(email, userQuery, llmResponse):
    sendurl = f"{db_url}{email}/add-message"
    payload = json.dumps({
        userQuery :llmResponse
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", sendurl, headers=headers, data=payload)

    print(response.json)

def get_conversation_history(email):
    geturl = f"{db_url}{email}/recent-messages"

    headers = {
        'accept': 'application/json'
    }
    response = requests.get(geturl, headers=headers)

    # print(response.json())  # Assuming the response is in JSON format
    data = response.json()
    return data["recent_messages"]
    
        