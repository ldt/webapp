from fastapi import FastAPI
from app.api.routers import auth, users
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# Include routers
app.include_router(auth.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the web app with user management!"}