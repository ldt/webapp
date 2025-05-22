from fastapi import APIRouter, Depends
from app.core.auth import auth_backend, fastapi_users

router = APIRouter()

# Register routes
router.register(auth_backend)
router.include_router(
    fastapi_users.get_register_router(),
)

# Login routes
router.include_router(
    fastapi_users.get_login_router(),
)