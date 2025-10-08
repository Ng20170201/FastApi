from typing import Optional, List

from fastapi import APIRouter, Request, HTTPException


router = APIRouter()


@router.get("/", summary="Root endpoint")
async def read_root():
    return {"message": "Hello, FastAPI with Swagger and MongoDB!"}
