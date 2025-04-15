from fastapi import FastAPI
from .api.meetings import router  # Import the router from your versioned API

app = FastAPI()

# Include API router for versioning
app.include_router(router, tags=["meetings"])
