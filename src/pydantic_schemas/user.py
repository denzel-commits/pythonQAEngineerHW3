from pydantic import BaseModel
from src.pydantic_schemas.book import Book


class User(BaseModel):
    name: str
    gender: str
    address: str
    age: int
    books: list[Book]
