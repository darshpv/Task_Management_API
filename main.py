from fastapi import FastAPI
from task_management.routes import router

app = FastAPI(
    title="Task Management API",
    version="0.1.0"
)

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Task Management API is Running"}

