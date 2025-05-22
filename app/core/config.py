from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "WebApp"
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()