from fastapi import FastAPI
from .api.meetings import router
app = FastAPI()

# Include API router for versioning
app.include_router(router, tags=["meetings"])
