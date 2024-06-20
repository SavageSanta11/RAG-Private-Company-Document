from fastapi import FastAPI
from routes.user import user 
import uvicorn

app = FastAPI()


app.include_router(user)

def start():
    uvicorn.run("index:app", host="0.0.0.0", port=8080, reload=True)

