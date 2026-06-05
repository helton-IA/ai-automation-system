from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import Task
from ..schemas import AutomationTask, TaskStatusUpdate

router = APIRouter(
    prefix="/automation/tasks",
    tags=["Automation Tasks"]
)


@router.post("")
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


@router.get("")
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


@router.get("/{task_id}")
def get_task(task_id: int):
    db: Session = SessionLocal()

    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    result = {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "priority": task.priority,
        "status": task.status
    }

    db.close()

    return result


@router.put("/{task_id}/status")
def update_task_status(task_id: int, status_update: TaskStatusUpdate):
    db: Session = SessionLocal()

    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

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


@router.delete("/{task_id}")
def delete_task(task_id: int):
    db: Session = SessionLocal()

    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(task)
    db.commit()
    db.close()

    return {
        "message": "Task deleted successfully",
        "task_id": task_id
    }