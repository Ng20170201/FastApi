from fastapi import FastAPI
import uvicorn

# Import the router from the controller using package absolute path. This is
# reliable both when running via `uvicorn app.main:app` and `python -m uvicorn`.
from app.Controller.controler import router as controller_router


app = FastAPI(
    title="Sample FastAPI with Swagger",
    description="A minimal FastAPI application that exposes Swagger UI at /docs",
    version="0.1.0",
)

# Include routes from the controller
app.include_router(controller_router)

# MongoDB lifecycle events (use absolute import)
from app.db import connect_to_mongo, close_mongo_connection


@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo(app)


@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection(app)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)