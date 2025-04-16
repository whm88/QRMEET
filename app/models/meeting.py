from sqlalchemy import Column, String, Date, Time, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(String(36), primary_key=True, index=True)
    title = Column(String(255))
    date = Column(Date)
    time = Column(Time)
    user_name = Column(String(100))
    email = Column(String(100))
    confirmed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    phone = Column(String(255), nullable=True)
    department = Column(String(50))
