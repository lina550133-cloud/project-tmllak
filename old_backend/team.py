from fastapi import APIRouter

router = APIRouter(prefix="/team", tags=["Team"])

@router.get("")
def team_members():
    return [
        {"name": "رغد", "email": "tmllak123.@gmail.com"},
        {"name": "غلا", "email": "tmllak123.@gmail.com"},
        {"name": "جود", "email": "tmllak123.@gmail.com"},
        {"name": "راما", "email": "tmllak123.@gmail.com"},
    ]
