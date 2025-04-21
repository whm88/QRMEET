import uuid
from sqlalchemy.orm import Session
from app.models.meeting import Meeting


def create_meeting(db: Session, data: dict) -> str:
    meeting_id = str(uuid.uuid4())
    meeting = Meeting(
        id=meeting_id,
        reason=data.get("reason"),
        date=data.get("date"),
        time=data.get("time"),
        user_name=data.get("user_name"),
        email=data.get("email"),
        department=data.get("department"),
        phone=data.get("phone"),
        confirmed=False,
    )
    db.add(meeting)
    db.commit()
    return meeting_id


def update_meeting(db: Session, meeting_id: str, data: dict):
    meeting = db.query(Meeting).filter(Meeting.id == meeting_id).first()
    if not meeting:
        return None
    meeting.reason = data["reason"]
    meeting.date = data["date"]
    meeting.time = data["time"]
    meeting.user_name = data["user_name"]
    meeting.email = data["email"]
    meeting.department=data["department"]
    meeting.phone=data["phone"]
    meeting.confirmed = True
    db.commit()
    return meeting


def get_meeting(db: Session, meeting_id: str):
    return db.query(Meeting).filter(Meeting.id == meeting_id).first()
