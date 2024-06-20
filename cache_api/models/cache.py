from pydantic import BaseModel
from typing import List, Dict

class CacheEntry(BaseModel):
    chunk_id: str
    entry_info : Dict

class UpdateModel(BaseModel):
    chunk_id: str
    new_access_time: float