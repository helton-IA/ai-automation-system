from enum import Enum
from pydantic import BaseModel


class TaskStatus(str, Enum):
    pending = "pending"
    running = "running"
    completed = "completed"
    failed = "failed"


class AutomationTask(BaseModel):
    title: str
    description: str
    priority: str = "medium"
    status: TaskStatus = TaskStatus.pending


class TaskStatusUpdate(BaseModel):
    status: TaskStatus

class LoginRequest(BaseModel):
    username: str
    password: str