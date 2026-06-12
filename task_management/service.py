import logging
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from task_management.models import Task, TaskStatus
from task_management.repository import TaskRepository, UserRepository
from task_management.schemas import TaskCreateRequest, TaskUpdateRequest


logger = logging.getLogger(__name__)

taskRepository = TaskRepository()
userRepository = UserRepository()


async def create_task(db: AsyncSession, task_data: TaskCreateRequest):
    logger.info(f"Creating task (assigned_to={task_data.assigned_to})")

    if task_data.assigned_to is None:
        logger.error("Task creation failed (assigned_to=None)")
        raise HTTPException(status_code=400, detail="Task must be assigned to a user")

    user = await userRepository.get_user_by_id(db=db, user_id=task_data.assigned_to)

    if not user:
        logger.error(f"Invalid assignee (user_id={task_data.assigned_to})")
        raise HTTPException(status_code=400, detail="Invalid user assigned")

    task = Task(
        title=task_data.title,
        description=task_data.description,
        status=task_data.status,
        assigned_to=task_data.assigned_to
    )

    created_task = await taskRepository.create_task(db=db, task_data=task)

    logger.info(f"Task created successfully (task_id={created_task.id})")

    return created_task


async def get_task(db: AsyncSession, task_id: int):
    logger.info(f"Fetching task (task_id={task_id})")

    task = await taskRepository.get_task_by_id(db=db, task_id=task_id)

    if not task:
        logger.error(f"Task not found (task_id={task_id})")
        raise HTTPException(status_code=404, detail="Task not found")

    return task


async def update_task(db: AsyncSession, task_id: int, task_data: TaskUpdateRequest):
    logger.info(f"Updating task (task_id={task_id})")

    task = await taskRepository.get_task_by_id(db=db, task_id=task_id)

    if not task:
        logger.error(f"Task not found for update (task_id={task_id})")
        raise HTTPException(status_code=404, detail="Task not found")

    update_data = task_data.model_dump(exclude_unset=True)

    if "assigned_to" in update_data and update_data["assigned_to"] is not None:
        user = await userRepository.get_user_by_id(db=db, user_id=task.assigned_to)
        if not user:
            logger.error(f"Invalid assignee during update (user_id={update_data['assigned_to']})")
            raise HTTPException(status_code=400, detail="Invalid user assigned")

    updated_task = await taskRepository.update_task(
        db=db,
        task_id=task_id,
        update_data=update_data
    )

    logger.info(f"Task updated successfully (task_id={task_id})")

    return updated_task


async def delete_task(db: AsyncSession, task_id: int):
    logger.info(f"Deleting task (task_id={task_id})")

    task = await taskRepository.get_task_by_id(db=db, task_id=task_id)

    if not task:
        logger.error(f"Task not found for deletion (task_id={task_id})")
        raise HTTPException(status_code=404, detail="Task not found")

    if task.status == TaskStatus.COMPLETED:
        logger.error(f"Cannot delete completed task (task_id={task_id})")
        raise HTTPException(status_code=400, detail="Cannot delete completed task")

    await taskRepository.delete_task(db=db, task_id=task_id)

    logger.info(f"Task deleted successfully (task_id={task_id})")


async def list_tasks(db: AsyncSession):
    logger.info("Listing all tasks")

    tasks = await taskRepository.list_tasks(db=db)

    if not tasks:
        logger.error("No tasks found")
        raise HTTPException(status_code=404, detail="No tasks found")

    return tasks
