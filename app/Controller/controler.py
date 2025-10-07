from typing import Optional, List

from fastapi import APIRouter, Request, HTTPException
from bson import ObjectId


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
    db = request.app.state.mongodb
    try:
        oid = ObjectId(item_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid item id")
    doc = await db.items.find_one({"_id": oid})
    if not doc:
        raise HTTPException(status_code=404, detail="Item not found")
    doc["_id"] = str(doc.get("_id"))
    return doc
