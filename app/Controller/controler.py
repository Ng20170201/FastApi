from typing import Optional, List

from fastapi import APIRouter, Request, HTTPException


router = APIRouter()


@router.get("/", summary="Root endpoint")
async def read_root():
    return {"message": "Hello, FastAPI with Swagger and MongoDB!"}


@router.get("/items/", summary="List items")
async def list_items(request: Request):
    db = request.app.state.mongodb
    cursor = db.items.find()
    items = []
    async for doc in cursor:
        # convert ObjectId to str for JSON serialization
        doc["_id"] = str(doc.get("_id"))
        items.append(doc)
    return items


@router.get("/items/{item_id}", summary="Read an item")
async def read_item(item_id: str, request: Request):
    return 1
