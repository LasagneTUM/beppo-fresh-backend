from typing import Union, List, cast
import json

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from models.models import UserPreferenceUpdate, Ingredient, Recipe, Option

from storage import add_multiple_preferences, get_preference_or_create, all_recipes, save_recipe_data, recipe_collection, preference_collection, get_recipe_by_id
from data.options import options

from .ranking import rank

fastapi_app = FastAPI()

origins = [
    "*"
]

fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

preference_collection.delete_many({})
recipe_collection.delete_many({})

with open("data/mockedIngredients.json") as f:
    ingredients = json.load(f)["ingredients"]

with open("data/mockedRecipes.json") as f:
    recipes = json.load(f)
    recipes = [i['recipe'] for i in recipes]
    save_recipe_data(recipes)

def get_ranked(user) -> List[Recipe]:
    user_obj = get_preference_or_create(cast(str, user))
    recipes = all_recipes()
    ranked = rank(user_obj, recipes)
    return ranked

@fastapi_app.get("/recommendations", response_model=list[Recipe])
async def recommendations(request: Request):
    user = request.headers.get("user")
    ranked = get_ranked(user)
    return ranked

@fastapi_app.get("/ingredients", response_model=list[Ingredient])
async def get_ingredients():
    return [
        Ingredient(name=i["name"], type=i["type"], imageLink=i["imageLink"],) for i in ingredients
    ]

@fastapi_app.post("/preferences/add", response_model=list[Recipe])
async def add_preferences(userPreferences: UserPreferenceUpdate):
    add_multiple_preferences(userPreferences)
    user = userPreferences.user
    return get_ranked(user)

@fastapi_app.get("/options", response_model=list[Option])
async def get_options():
    return options

@fastapi_app.get("/recipe/{recipe_id}", response_model=Recipe)
async def get_recipe(recipe_id: str):
    return get_recipe_by_id(recipe_id)

    

