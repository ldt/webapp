from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication, CookieTransport
from fastapi_users.db import SQLAlchemyUserDatabase
from app.core.config import settings
from app.models.user import User
from app.db.session import get_user_db

class JWTAuth(JWTAuthentication):
    def __init__(self):
        super().__init__(
            secret=settings.SECRET_KEY,
            lifetime_seconds=3600,  # 1 hour
            tokenUrl="/auth/login",
        )

cookie_transport = CookieTransport(secure=False, max_age=3600)

def get_jwt_strategy() -> JWTAuth:
    return JWTAuth()

auth_backend = JWTAuth()
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

async def get_user_db():
    yield SQLAlchemyUserDatabase(User, get_user_manager())

async def get_user_manager(user_db=Depends(get_user_db)):
    yield user_db

current_active_user = fastapi_users.current_user(active=True)