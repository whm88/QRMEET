import uuid
from sqlalchemy.orm import Session
from app.models.meeting import Meeting


def create_meeting(db: Session, data: dict) -> str:
    meeting_id = str(uuid.uuid4())
    meeting = Meeting(
        id=meeting_id,
        reason=data.get("reason"),
        user_name=data.get("user_name"),
        company=data.get("company"),
        email=None,
        department=None,
        confirmed=False,
    )
    db.add(meeting)
    db.commit()
    return meeting_id


def update_meeting(db: Session, meeting_id: str, data: dict):
    meeting = db.query(Meeting).filter(Meeting.id == meeting_id).first()
    if not meeting:
        return None
    
    meeting.reason = data.get("reason", meeting.reason)
    meeting.user_name = data.get("user_name", meeting.user_name)
    meeting.company = data.get("company", meeting.company)
    meeting.email = data.get("email")
    meeting.department = data.get("department")
    meeting.confirmed = True
    db.commit()
    return meeting


def get_meeting(db: Session, meeting_id: str):
    return db.query(Meeting).filter(Meeting.id == meeting_id).first()