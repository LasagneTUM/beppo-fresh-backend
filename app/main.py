from typing import Union
import json

from fastapi import FastAPI, Request

from .models import UserPreference

from storage import add_preference, remove_preference, get_preference

fastapi_app = FastAPI()

with open("data/mockedIngredients.json") as f:
    ingredients = json.load(f)["ingredients"]

with open("data/mockedRecipes.json") as f:
    recipes = json.load(f)
    recipes = [i['recipe'] for i in recipes]

options = [
    ["rice", "noodels"],
    ["beans", "lentils"],
    ["crean", "coconut milk"],
    ["chicken stock", "vegetable stock"],
    ["gouda", "cheddar"]
]

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

@fastapi_app.post("/preferences/add")
async def add_preferences(userPreference: UserPreference):
    add_preference(userPreference.user, userPreference.preference)
    return recipes

@fastapi_app.post("/preferences/remove")
async def remove_preferences(userPreference: UserPreference):
    remove_preference(userPreference.user, userPreference.preference)
    return recipes

@fastapi_app.get("/preferences")
async def get_preferences(request: Request):
    user = request.headers.get("user")
    return get_preference(user)

@fastapi_app.get("/options")
async def get_options():
    return options
    

