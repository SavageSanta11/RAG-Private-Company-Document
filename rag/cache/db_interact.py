cache_url = None # replace with cache api deployment URL

import requests
import json

def update_cache_entry(chunk_id, new_access_time):
    sendurl = f"{cache_url}/update"
    payload = json.dumps({
        "chunk_id" : chunk_id,
        "new_access_time": new_access_time
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", sendurl, headers=headers, data=payload)
    data = response.json()
    return data

def add_to_cache(cache_info_dict):
    sendurl = f"{cache_url}/create"
    payload = json.dumps(cache_info_dict)
    headers = {
        'accept': 'application/json'
    }
    response = requests.request("POST", sendurl, headers=headers, data=payload)

    # print(response.json())  # Assuming the response is in JSON format
    data = response.json()
    return data

def get_faqs():
    geturl = f"{cache_url}/faq"

    headers = {
        'accept': 'application/json'
    }
    response = requests.get(geturl, headers=headers)

    # print(response.json())  # Assuming the response is in JSON format
    data = response.json()
    return data