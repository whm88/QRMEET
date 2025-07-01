from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(String(36), primary_key=True, index=True)
    reason = Column(String(255))
    user_name = Column(String(100))
    company = Column(String(100))
    email = Column(String(100), nullable=True)
    department = Column(String(50), nullable=True)
    confirmed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "reason": self.reason,
            "user_name": self.user_name,
            "company": self.company,
            "email": self.email,
            "department": self.department,
            "confirmed": self.confirmed,
            "created_at": self.created_at,
        }