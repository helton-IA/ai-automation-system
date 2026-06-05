from fastapi import FastAPI

from .database import engine, Base
from .config import APP_NAME, APP_VERSION
from .routers.tasks import router as tasks_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)

app.include_router(tasks_router)


@app.get("/")
def health_check():
    return {
        "status": "online",
        "message": "AI Automation System is running successfully."
    }