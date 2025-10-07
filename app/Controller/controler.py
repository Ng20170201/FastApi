from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@router.get("/", summary="Root endpoint")
def read_root():
    return {"message": "Hello, FastAPI with Swagger!"}


@router.get("/items/{item_id}", summary="Read an item")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@router.post("/items/", summary="Create an item", response_model=Item)
def create_item(item: Item):
    return item
