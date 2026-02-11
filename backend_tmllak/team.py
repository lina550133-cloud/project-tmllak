from fastapi import APIRouter

router = APIRouter()

@router.get("/team")
def get_team():
    return {"team": ["lina", "raghad", "rama"]}
