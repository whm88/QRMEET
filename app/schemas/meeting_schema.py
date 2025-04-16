from pydantic import BaseModel
from datetime import date, time, datetime
from typing import Optional


class MeetingBase(BaseModel):
    title: str
    date: date
    time: time
    user_name: str
    email: str
    phone: str
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
