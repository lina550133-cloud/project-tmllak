from fastapi import APIRouter

router = APIRouter(prefix="/profile", tags=["Profile"])

@router.get("")
def get_profile():
    return {
        "email": "Ahmed@icloud.com",
        "phone": None,
        "location": None,
        "sessions": 3
    }
