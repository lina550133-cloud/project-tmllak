from fastapi import APIRouter

router = APIRouter(prefix="/clients", tags=["Clients"])

@router.get("")
def list_clients():
    return [
        {"name": "مالك", "phone": "560 05", "email": None}
    ]
