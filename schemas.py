from datetime import date
from typing import Literal, Optional
from pydantic import BaseModel, ConfigDict
Status = Literal["Not Started", "Ongoing", "Completed", "Delayed"]
Topic = Literal["Digital", "Data", "AI"]
class ProjectBase(BaseModel):
    name: str
    country: str
    owner: Optional[str] = None
    topic: Optional[Topic] = None
    status: Status = "Not Started"
    next_milestone: Optional[str] = None
    milestone_date: Optional[date] = None
    status_note: Optional[str] = None
class ProjectCreate(ProjectBase):
    pass
class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    country: Optional[str] = None
    owner: Optional[str] = None
    topic: Optional[Topic] = None
    status: Optional[Status] = None
    next_milestone: Optional[str] = None
    milestone_date: Optional[date] = None
    status_note: Optional[str] = None
class ProjectOut(ProjectBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
