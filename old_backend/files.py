from fastapi import APIRouter

router = APIRouter(prefix="/files", tags=["Files"])

@router.get("")
def list_files():
    return [
        {"name": "Contract.pdf", "type": "PDF", "date": "2024-10-05"},
        {"name": "Deed.pdf", "type": "PDF", "date": "2024-10-04"},
    ]
