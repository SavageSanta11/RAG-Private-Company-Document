from typing import List
from pydantic import BaseModel


class AskQuestionRequest(BaseModel):
    question: str
    email: str


class GetFileRequest(BaseModel):
    file_name: str


class UpsertFilesResponse(BaseModel):
    success: bool


class AskQuestionResponse(BaseModel):
    answer: str
    sources: List[str]

class GetCacheQuestions(BaseModel):
    freq_questions: List


