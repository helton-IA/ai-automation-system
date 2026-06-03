from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session

from .database import engine, SessionLocal, Base
from .models import Task

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Automation System",
    version="3.0.0"
)

class AutomationTask(BaseModel):
    title: str
    description: str
    priority: str = "medium"
    status: str = "pending"

@app.get("/")
def health_check():
    return {
        "status": "online",
        "message": "AI Automation System is running successfully."
    }

@app.post("/automation/tasks")
def create_task(task: AutomationTask):
    db: Session = SessionLocal()

    new_task = Task(
        title=task.title,
        description=task.description,
        priority=task.priority,
        status=task.status
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    db.close()

    return {
        "message": "Task created successfully",
        "task": {
            "id": new_task.id,
            "title": new_task.title,
            "description": new_task.description,
            "priority": new_task.priority,
            "status": new_task.status
        }
    }

@app.get("/automation/tasks")
def list_tasks():
    db: Session = SessionLocal()

    tasks = db.query(Task).all()

    result = []

    for task in tasks:
        result.append({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "priority": task.priority,
            "status": task.status
        })

    db.close()

    return {
        "total": len(result),
        "tasks": result
    }

class TaskStatusUpdate(BaseModel):
    status: str



@app.put("/automation/tasks/{task_id}/status")
def update_task_status(task_id: int, status_update: TaskStatusUpdate):
    db: Session = SessionLocal()

    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        db.close()
        return {
            "error": "Task not found"
        }

    task.status = status_update.status

    db.commit()
    db.refresh(task)

    db.close()

    return {
        "message": "Task status updated successfully",
        "task": {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "priority": task.priority,
            "status": task.status
        }
    }
@app.delete("/automation/tasks/{task_id}")
def delete_task(task_id: int):
    db: Session = SessionLocal()

    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        db.close()
        return {
            "error": "Task not found"
        }

    db.delete(task)
    db.commit()
    db.close()

    return {
        "message": "Task deleted successfully",
        "task_id": task_id
    }
@app.get("/automation/tasks/{task_id}")
def get_task(task_id: int):

    db: Session = SessionLocal()

    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        db.close()

        return {
            "error": "Task not found"
        }

    result = {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "priority": task.priority,
        "status": task.status
    }

    db.close()

    return result