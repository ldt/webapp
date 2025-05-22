from fastapi import APIRouter, Depends
from app.core.auth import auth_backend, current_active_user

router = APIRouter()

@router.get("/users/me")
def read_users_me(current_user=Depends(current_active_user)):
    return current_user