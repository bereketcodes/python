from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Fake "database" — just a Python list, for now
fake_db = []

class Task(BaseModel):
    title: str
    done: bool = False

@app.get("/tasks")
def list_tasks():
    return fake_db

@app.post("/tasks")
def create_task(task: Task):
    fake_db.append(task)
    return {"message": "Task added", "total_tasks": len(fake_db)}

@app.get("/tasks/{task_index}")
def get_task(task_index: int):
    if task_index < 0 or task_index >= len(fake_db):
        return {"error": "Task not found"}
    return fake_db[task_index]
@app.get("/square/{number}")
def get_square(number: int):
    return {"number": number, "square": number ** 2}
@app.delete("/tasks/{task_index}")
def delete_task(task_index: int):
    if task_index < 0 or task_index >= len(fake_db):
        return {"error": "Task not found"}
    deleted_task = fake_db.pop(task_index)
    return {"message": "Task deleted", "deleted_task": deleted_task}