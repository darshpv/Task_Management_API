from http.client import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models import Task, User, TaskStatus
from core.database import SessionLocal
from schemas import TaskCreateRequest


class TaskRepository:

    async def create_task(self, db: AsyncSession, task_data: Task):
        try:
            new_task = Task(
                title=task_data.title,
                description=task_data.description,
                status=task_data.status, 
                assigned_to=task_data.assigned_to
            )
            db.add(new_task)
            await db.commit()
            await db.refresh(new_task)

        except Exception as e:
            await db.rollback()
            raise e

    async def get_task_by_id(self, task_id: int, db: AsyncSession):
        try:
            result = await db.execute(
                select(Task).where(Task.id == task_id)
            )
            result_task = result.scalar_one_or_none()
            # if not result_task:
            #     raise HTTPException(detail="Task not found")
            return result_task
        
        except Exception as e:
            await db.rollback()
            raise e

    async def update_task(self, db: AsyncSession, task_id: int, update_data: dict):

        try:
            result = await db.execute(
                select(Task).where(Task.id == task_id)
            )

            task = result.scalar_one()

            for field, value in update_data:
                if value is not None:
                    setattr(task, field, value)

            await db.commit()
            await db.refresh(task)

        except Exception as e:
            await db.rollback()
            raise e

    async def delete_task(self, db: AsyncSession, task_id: int):

        try:
            result = await db.execute(
                select(Task).where(Task.id == task_id)
            )

            task = result.scalar_one()

            await db.delete(task)
            await db.commit()

        except Exception as e:
            await db.rollback()
            raise e

    async def list_tasks(self, db: AsyncSession):

        try:
            result = await db.execute(
                select(Task)
            )

            tasks = result.scalars().all()

            return tasks
        
        except Exception as e:
            await db.rollback()
            raise e

class UserRepository:

    async def get_user_by_id(self, user_id: int, db: AsyncSession):
        try:
            result = await db.execute(
                select(User).where(User.id == user_id)
            )
            result_user = result.scalar_one_or_none()
            # if not result_task:
            #     raise HTTPException(detail="Task not found")
            return result_user
        
        except Exception as e:
            await db.rollback()
            raise e