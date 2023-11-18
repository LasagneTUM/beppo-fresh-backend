# BeppoFresh Backend

## About
This the backend repository for the project "BeppoFresh" by LasagneTUM for the HelloFresh Challenge at HackaTUM 2023

## Run

- Create venv `python3 -m venv venv`
- Activate venv `source venv/bin/activate`
- Install pip tools `pip install pip-tools`
- Generate requirements.txt `pip-compile requirements.in`
- Install requirements.txt `pip install -r requirements.txt`
- Run server `uvicorn main:app --reload`