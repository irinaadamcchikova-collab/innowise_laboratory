from pydantic import BaseModel
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str
    year: Optional[int] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None

class BookInDB(BookBase):
    id: int

    class Config:
        from_attributes = True