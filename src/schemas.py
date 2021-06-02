from datetime import datetime

from pydantic import BaseModel


class TaskRaw(BaseModel):
    num: int
    timeout: int


class Task(TaskRaw):
    order: int
    created_at: datetime
