from typing import Optional
import os

from motor.motor_asyncio import AsyncIOMotorClient


MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb://localhost:27017")
DB_NAME = os.environ.get("MONGODB_DB", "short_url_db")


def get_database(app):
    """Return the Motor database instance stored on the FastAPI app state."""
    return app.state.mongodb


async def connect_to_mongo(app):
    client = AsyncIOMotorClient(MONGODB_URI)
    app.state.mongodb_client = client
    app.state.mongodb = client[DB_NAME]


async def close_mongo_connection(app):
    client: Optional[AsyncIOMotorClient] = getattr(app.state, "mongodb_client", None)
    if client:
        client.close()
