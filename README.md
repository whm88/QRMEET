# QRMeet - FastAPI Application

QRMeet is a FastAPI-based application that handles meetings, their creation, retrieval, and updates. This project uses SQLite as the database and integrates tests using `pytest` with a mock in-memory database for testing purposes.

## Features

- **Create Meetings**: Allows users to create new meetings with details like reason, user name, email, date, and time.
- **Get Meetings**: Retrieve meetings by ID.
- **Update Meetings**: Update details of an existing meeting.

## Prerequisites

- Python 3.11+
- Poetry for dependency management

## How to get started

poetry install

poetry shell

poetry run uvicorn app.main:app --reload

