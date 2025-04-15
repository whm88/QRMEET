from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.models.meeting import Base  # Import Base from your models to access metadata

# Define the database URL
DATABASE_URL = settings.database_url

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session local class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Function to create tables if they don't exist
def create_tables():
    Base.metadata.create_all(bind=engine)  # This creates tables from the Base metadata


# Function to get a session for querying the database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Optionally, create tables when the app starts (or on the first access to the database)
create_tables()
