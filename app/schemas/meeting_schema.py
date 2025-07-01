from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class MeetingBase(BaseModel):
    reason: str
    user_name: str
    company: str
    email: Optional[str] = None 
    department: Optional[str] = None


class MeetingCreate(BaseModel):
    reason: str
    user_name: str
    company: str


class MeetingUpdate(BaseModel):
    reason: str
    user_name: str
    company: str
    email: str
    department: str


class MeetingResponse(MeetingBase):
    id: str
    confirmed: bool
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = (
            True  # This allows SQLAlchemy models to be converted to Pydantic models
        )


class MeetingCreateResponse(BaseModel):
    meeting_id: str


class MeetingUpdateResponse(BaseModel):
    message: str
    status: str
