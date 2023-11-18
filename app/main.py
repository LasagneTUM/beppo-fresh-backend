from typing import Union

from fastapi import FastAPI

fastapi_app = FastAPI()

@fastapi_app.get("/")
def read_root():
    return {"Hello": "World"}


@fastapi_app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
