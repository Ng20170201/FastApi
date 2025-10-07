from fastapi import FastAPI

# Import the router from the controller. Use a try/except so the module can be
# executed both as a script (cwd=app) and as a package (uvicorn app.main:app).
try:
    from Controller.controler import router as controller_router
except Exception:
    from app.Controller.controler import router as controller_router


app = FastAPI(
    title="Sample FastAPI with Swagger",
    description="A minimal FastAPI application that exposes Swagger UI at /docs",
    version="0.1.0",
)

# Include routes from the controller
app.include_router(controller_router)

# MongoDB lifecycle events
try:
    from .db import connect_to_mongo, close_mongo_connection
except Exception:
    from db import connect_to_mongo, close_mongo_connection


@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo(app)


@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection(app)

