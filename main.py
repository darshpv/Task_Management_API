from fastapi import FastAPI
from task_management.routes import router

app = FastAPI()

app.include_router(router)