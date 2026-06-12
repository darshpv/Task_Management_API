from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from core.dependencies import get_current_user_id
from core.database import get_db_session
from task_management.schemas import (
    TaskCreateRequest,
    TaskUpdateRequest,
    TaskResponse
)
from task_management import service

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskResponse, status_code=201)
async def create_task(
    task_data: TaskCreateRequest,
    db: AsyncSession = Depends(get_db_session),
    user_id: int = Depends(get_current_user_id)
):
    return await service.create_task(db=db, task_data=task_data)

@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(
    task_id: int,
    db: AsyncSession = Depends(get_db_session)
):
    return await service.get_task(db=db, task_id=task_id)

@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: int,
    update_data: TaskUpdateRequest,
    db: AsyncSession = Depends(get_db_session),
    user_id: int = Depends(get_current_user_id)
):
    return await service.update_task(db=db, task_id=task_id, task_data=update_data)

@router.delete("/{task_id}")
async def delete_task(
    task_id: int,
    db: AsyncSession = Depends(get_db_session),
    user_id: int = Depends(get_current_user_id)
):
    await service.delete_task(db=db, task_id=task_id)
    return

@router.get("/", response_model=List[TaskResponse])
async def list_tasks(
    db: AsyncSession = Depends(get_db_session)
):
    return await service.list_tasks()