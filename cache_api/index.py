from fastapi import FastAPI
from routes.cache import cache 
import uvicorn

app = FastAPI()


app.include_router(cache)

def start():
    uvicorn.run("index:app", host="0.0.0.0", port=8000, reload=True)

