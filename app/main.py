from typing import Union
import json

from fastapi import FastAPI, Request

fastapi_app = FastAPI()

with open("data/mockedIngredients.json") as f:
    ingredients = json.load(f)["ingredients"]

with open("data/mockedRecipes.json") as f:
    recipes = json.load(f)
    recipes = [i['recipe'] for i in recipes]

@fastapi_app.get("/")
async def read_root():
    return {"Hello": "World"}

@fastapi_app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@fastapi_app.get("/recommendations")
async def recommendations(request: Request):
    user = request.headers.get("user")
    return recipes

@fastapi_app.get("/ingredients")
async def get_ingredients():
    return ingredients

