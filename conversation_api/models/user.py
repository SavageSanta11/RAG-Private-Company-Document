from pydantic import BaseModel
from typing import List, Dict

class User(BaseModel):
    email: str
    message:List[Dict[str,str]]

