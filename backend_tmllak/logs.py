from fastapi import APIRouter

router = APIRouter(prefix="/logs", tags=["Logs"])

@router.get("")
def logs():
    return [
        {"task": "المهمة 1", "status": "تم الانتهاء", "date": "2026-02-01"},
        {"task": "المهمة 2", "status": "قيد العمل", "date": "2026-02-02"},
    ]
