from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserModel
from sqlalchemy import Column, Integer, String, Boolean
from app.db.base import Base

class User(SQLAlchemyBaseUserModel[int], Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, unique=True)
    hashed_password = Column(String(length=1024), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)