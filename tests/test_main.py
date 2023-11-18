from fastapi.testclient import TestClient

from app.main import fastapi_app
client = TestClient(fastapi_app)