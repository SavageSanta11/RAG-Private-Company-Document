import os
import uvicorn
from fastapi import FastAPI, File, HTTPException, Depends, Body, UploadFile, Request
from typing import List
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import urlparse
import time
from vectorstore import PineconeVectorStore
from cache.cache_db import CacheVectorStore
from llm import get_selected_llm
from models.api import (
    AskQuestionRequest,
    AskQuestionResponse,
    GetCacheQuestions
)
from conv_history.db_interact import send_message_to_conversation_db, get_conversation_history

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to the list of allowed origins if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

bearer_scheme = HTTPBearer()
vector_store = PineconeVectorStore()
cache_vector_store = CacheVectorStore()
llm = get_selected_llm()


@app.get("/")
async def test_server():
    return {"Server is up!"}

@app.get("/freq-questions",response_model=GetCacheQuestions)
async def get_freq_questions(request: Request):
    try:
        freq_questions = await cache_vector_store.get_frequent()
        return GetCacheQuestions(
            freq_questions=freq_questions
        )
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    
# @app.get("/clear-cache")
# async def clear_cache(request: Request):
#     try:
#         status = await cache_vector_store.clear_cache()
#         return status
#     except Exception as e:
#         print(e)
#         raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/ask-question",response_model=AskQuestionResponse)
async def ask_question(request: AskQuestionRequest = Body(...),):
    try:
        question = request.question
        email = request.email

        response = await cache_vector_store.search_cache(question)
        
        if response is None:
            documents = await vector_store.query(question)
            print(documents)
            conv_history = get_conversation_history(email)
            answer = await llm.ask(documents, question, conv_history)
            print(answer)
            send_message_to_conversation_db(email, question, answer)
            question_cache_status = await cache_vector_store.add_to_cache(query=question, answer=answer, chunk_id=None)
            print(question_cache_status)
            return AskQuestionResponse(
                answer=answer, sources=[doc.title for doc in documents]
            )
        else:
            send_message_to_conversation_db(email, question, response)
            return AskQuestionResponse(
                answer=response, sources=[]
            )
        
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))


def start():
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
