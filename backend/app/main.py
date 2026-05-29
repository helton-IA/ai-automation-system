from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="AI Automation System",
    version="1.0.0"
)

class AutomationTask(BaseModel):
    title: str
    description: str
    priority: str = "medium"

tasks = []

@app.get("/")
def health_check():
    return {
        "status": "online",
        "message": "AI Automation System is running successfully."
    }

@app.get("/automation/tasks")
def list_tasks():
    return {
        "total": len(tasks),
        "tasks": tasks
    }
