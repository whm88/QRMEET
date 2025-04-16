import uuid
from sqlalchemy.orm import Session
from app.models.meeting import Meeting


def create_meeting(db: Session, data: dict) -> str:
    meeting_id = str(uuid.uuid4())
    meeting = Meeting(
        id=meeting_id,
        title=data["title"],
        date=data["date"],
        time=data["time"],
        user_name=data["user_name"],
        email=data["email"],
        department=data["department"],
        phone=data["phone"],
        confirmed=False,
    )
    db.add(meeting)
    db.commit()
    return meeting_id


def update_meeting(db: Session, meeting_id: str, data: dict):
    meeting = db.query(Meeting).filter(Meeting.id == meeting_id).first()
    if not meeting:
        return None
    meeting.title = data["title"]
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
