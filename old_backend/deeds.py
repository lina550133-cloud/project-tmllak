from fastapi import APIRouter

router = APIRouter(prefix="/deeds", tags=["Deeds"])

@router.get("")
def list_deeds():
    return [
        {"status": "مسجل", "date": "2024-01-08", "owner": "—"}
    ]
