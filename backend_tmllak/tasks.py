from fastapi import APIRouter

router = APIRouter()

@router.get("/tasks")
def get_tasks():
    return {"tasks": ["Task 1", "Task 2", "Task 3"]}
