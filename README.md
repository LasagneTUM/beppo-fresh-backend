# BeppoFresh Backend

## About
This the backend repository for the project "BeppoFresh" by LasagneTUM for the HelloFresh Challenge at HackaTUM 2023

## Requirements
We use a MongoDB Server to store the data. There are different options how you can use one:
- Use MongoDB Atlas (managed service; we use it for the demo)
- Local installation
- With docker-compose

For the usage of docker-compose we provide a Dockerfile and docker-compose.yaml
- Build container `docker build . -t "beppo-fresh-backend"`
- Run compose`docker compose up -d`

**Important!**
Set the appropriate connection string for your database connection in .env with the variable 'MONGODB_CONNECTION'

## Run

- Create venv `python3 -m venv venv`
- Activate venv `source venv/bin/activate`
- Install pip tools `pip install pip-tools`
- Generate requirements.txt `pip-compile requirements.in`
- Install requirements.txt `pip install -r requirements.txt`
- Run server `uvicorn app.main:fastapi_app --reload`

## Test

Run `python3 -m pytest tests`

## Type checking

Run `python3 -m mypy -p app`