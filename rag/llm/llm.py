
from typing import List, Any, Optional
import uuid
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
import os
import requests
import json
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains.question_answering import load_qa_chain
from langchain.docstore.document import Document

from models.models import Document, LLM
def get_selected_llm():
    return Falcon7BLLM()

base_url = None # replace with model deployment URL

def extract_text_after_last_inst(sentence):
    last_inst_index = sentence.rfind('[/INST]')
    if last_inst_index != -1:
        return sentence[last_inst_index + len('[/INST]'):].strip()
    else:
        return sentence

# Example usage:
sentence = "This is a sample [INST]text[/INST] with multiple [INST]instances[/INST] of [INST]tags[/INST]"
extracted_text = extract_text_after_last_inst(sentence)
print(extracted_text)  # Output: 'tags'
class Falcon7BLLM(LLM):
    def __init__(self):
        super().__init__()

    async def ask(self, documents: List[Document], question: str, conv_history: str) -> str:
        context_str = ""

        # doc = documents[0]
        # context_str += f"{doc.title}: {doc.content}\n\n"

        context_str = ""  # Initialize an empty string to store the concatenated titles and contents

        for doc in documents:
            context_str += f"{doc.title}: {doc.content}\n\n"

        prompt = (
            "[INST] Context: \n"
            "---------------------\n"
            f"{context_str}"
            "\n---------------------\n"
            f"{conv_history}"
            "\n---------------------\n"
            f"You are a helpful employee of the company, DB Schenker. Given the above context, conversation history and no other information, answer the following company information related question: {question}\n [/INST]"
        )

        data = {"prompt": prompt}

        # res = requests.post(f"{base_url}:8080/v1/models/model:predict", json=data)
        res = requests.post(base_url, headers={"Authorization": "Api-Key IU5yVkWg.ut9kH4aDbIryBznMOiGhkNU8DBicSaHP"}, json=data)
        res_json = res.json()
        result = extract_text_after_last_inst(res_json)
        answer_without_end_token = result.replace("</s>", "")
        return answer_without_end_token