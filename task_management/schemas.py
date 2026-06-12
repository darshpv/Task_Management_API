from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from task_management.models import TaskStatus

class TaskCreateRequest(BaseModel):
    title: str = Field(..., min_length=5, max_length=100)
    description: str = Field(..., min_length=10, max_length=255)
    status: TaskStatus
    assigned_to: int

class TaskUpdateRequest(BaseModel):
    title: Optional[str] = Field(
        None,
        min_length=5,
        max_length=100
    )
    description: Optional[str] = Field(
        None,
        min_length=10,
        max_length=255
    )
    status: Optional[TaskStatus] = None
    assigned_to: Optional[int] = None
    
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: TaskStatus
    assigned_to: int

    model_config = ConfigDict(from_attributes=True)
