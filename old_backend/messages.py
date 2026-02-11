from fastapi import APIRouter

router = APIRouter(prefix="/messages", tags=["Messages"])

@router.get("")
def inbox():
    return [
        {"title": "رسالة من محمد", "priority": "عالية", "date": "2026-02-14"}
    ]

@router.post("/send")
def send_message(title: str, subject: str):
    return {"message": "Message sent"}
