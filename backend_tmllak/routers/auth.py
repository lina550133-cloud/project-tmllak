from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(email: str, password: str):
    return {"message": "Login successful", "email": email}

@router.post("/register")
def register(email: str, password: str, confirm_password: str):
    return {"message": "Account created"}
