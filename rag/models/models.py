from pydantic import BaseModel
from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from enum import Enum


class Document(BaseModel):
    id: str
    title: str
    content: str


class AppConfig(BaseModel):
    app_id: str
    user_id: str


class VectorStore(BaseModel, ABC):
    @abstractmethod
    async def upsert(self, documents: List[Document]) -> bool:
        pass

    @abstractmethod
    async def query(self, query: str) -> List[Document]:
        pass


class LLM(BaseModel, ABC):
    @abstractmethod
    def ask(self, documents: List[str], question: str, conv_history: str) -> List[List[float]]:
        pass
