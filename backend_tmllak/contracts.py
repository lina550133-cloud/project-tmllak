from fastapi import APIRouter

router = APIRouter(prefix="/contracts", tags=["Contracts"])

@router.get("")
def list_contracts():
    return [
        {"client": "Sheood", "value": "001.306", "contract": "Sand"}
    ]
