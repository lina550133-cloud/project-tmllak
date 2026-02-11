from fastapi import APIRouter

router = APIRouter(prefix="/home", tags=["Home"])

@router.get("")
def dashboard():
    return {
        "tasks": 8,
        "late_tasks": ["المهمة ١", "المهمة ٣"],
        "messages": 3,
        "workspace": "5.5 GB"
    }
