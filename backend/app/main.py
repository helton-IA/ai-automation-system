from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="AI Automation System",
    description="API profissional para gerenciamento de tarefas e fluxos de automação com IA.",
    version="2.0.0"
)

class AutomationTask(BaseModel):
    title: str
    description: str
    priority: str = "medium"
    status: str = "pending"

tasks = []

@app.get("/")
def health_check():
    return {
        "status": "online",
        "message": "AI Automation System is running successfully.",
        "version": "2.0.0"
    }

@app.post("/automation/tasks")
def create_task(task: AutomationTask):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "description": task.description,
        "priority": task.priority,
        "status": task.status
    }

    tasks.append(new_task)

    return {
        "message": "Task created successfully.",
        "task": new_task
    }

@app.get("/automation/tasks")
def list_tasks():
    return {
        "total": len(tasks),
        "tasks": tasks
    }

@app.get("/automation/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found.")

@app.put("/automation/tasks/{task_id}")
def update_task(task_id: int, updated_task: AutomationTask):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            task["description"] = updated_task.description
            task["priority"] = updated_task.priority
            task["status"] = updated_task.status

            return {
                "message": "Task updated successfully.",
                "task": task
            }

    raise HTTPException(status_code=404, detail="Task not found.")

@app.delete("/automation/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)

            return {
                "message": "Task deleted successfully.",
                "task": task
            }

    raise HTTPException(status_code=404, detail="Task not found.")
