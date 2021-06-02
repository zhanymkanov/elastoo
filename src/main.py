import asyncio
from datetime import datetime
from typing import List
from collections import deque

from fastapi import FastAPI, status

from .schemas import TaskRaw, Task

app = FastAPI()

queue = deque()
tasks = []
nums = []


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
async def create_task(data: TaskRaw):
    new_task = Task(**data.dict(), created_at=datetime.now(), order=len(tasks))
    queue.append(new_task)
    tasks.append(new_task)

    return new_task


@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return tasks


@app.get("/results", response_model=List[int])
async def get_results():
    return nums


async def worker():
    while 1:
        if queue:
            await execute_task()

        await asyncio.sleep(1)


async def execute_task():
    data = queue.popleft()

    try:
        await add_num(data)
    except Exception:  # hypothetical exception
        queue.append(data)


async def add_num(data: TaskRaw):
    await asyncio.sleep(data.timeout)
    nums.append(data.num)


asyncio.create_task(worker())
