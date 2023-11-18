FROM python:3.11.6

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY . .

CMD ["uvicorn", "app.main:fastapi_app", "--host", "0.0.0.0", "--port", "80"]