from fastapi import Request, APIRouter, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services import meeting_service
from app.schemas.meeting_schema import (
    MeetingBase,
    MeetingResponse,
    MeetingCreateResponse,
    MeetingUpdateResponse,
)

router = APIRouter()


# Create a new meeting
@router.post(
    "/meetings/",
    tags=["meetings"],
    status_code=status.HTTP_201_CREATED,
    response_model=MeetingCreateResponse,
)
def create_meeting(data: MeetingBase, db: Session = Depends(get_db)):
    meeting_id = meeting_service.create_meeting(db, data.dict())
    return MeetingCreateResponse(meeting_id=meeting_id)


# Update an existing meeting
@router.put(
    "/meetings/{meeting_id}",
    tags=["meetings"],
    status_code=status.HTTP_200_OK,
    response_model=MeetingUpdateResponse,
)
def update_meeting(meeting_id: str, data: MeetingBase, db: Session = Depends(get_db)):
    meeting = meeting_service.update_meeting(db, meeting_id, data.dict())
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")
    return MeetingUpdateResponse(message="Meeting confirmed", status ="success")


# Get a meeting by ID
@router.get(
    "/meetings/{meeting_id}",
    tags=["meetings"],
    status_code=status.HTTP_200_OK,
    response_model=MeetingResponse,
)
def get_meeting(meeting_id: str, db: Session = Depends(get_db)):
    meeting = meeting_service.get_meeting(db, meeting_id)
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")
    return meeting


templates = Jinja2Templates(directory="app/templates")


@router.get(
    "/ui/meetings/form",
    tags=["meetings"],
    response_class=HTMLResponse
)
def render_meeting_form(request: Request, meeting_id: str = None, db: Session = Depends(get_db)):
    print(request, meeting_id)
    meeting_data = None
    if meeting_id:
        meeting = meeting_service.get_meeting(db, meeting_id)
        if not meeting:
            raise HTTPException(status_code=404, detail="Meeting not found")
        meeting_data = meeting.to_dict()

    return templates.TemplateResponse(
        "meeting_form.html",
        {
            "request": request,
            "meeting": meeting_data
        }
    )
