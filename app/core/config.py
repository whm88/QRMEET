import secrets
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "QRMeet"
    database_url: str
    secret_key: str

    class Config:
        env_file = ".env"  # Load environment variables from .env file

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.secret_key:
            self.secret_key = secrets.token_urlsafe(32)


settings = Settings()
