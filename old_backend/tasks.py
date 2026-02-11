from fastapi import APIRouter

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("")
def list_tasks():
    return [
        {"title": "تجهيز عقد إيجار", "priority": "عالية", "status": "قيد التنفيذ"},
        {"title": "المهمة 1", "status": "تم الانتهاء"},
    ]

@router.get("/{task_id}")
def task_details(task_id: int):
    return {"task_id": task_id, "details": "تفاصيل المهمة"}
