from typing import Union, List, cast
import json

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from models.models import UserPreferenceUpdate, Ingredient, Recipe, Option

from storage import add_multiple_preferences, get_preference_or_create, all_recipes

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

with open("data/mockedIngredients.json") as f:
    ingredients = json.load(f)["ingredients"]

with open("data/mockedRecipes.json") as f:
    recipes = json.load(f)
    recipes = [i['recipe'] for i in recipes]

options = [
    Option(
        first_option=Ingredient(
            name="Teriyakisoße",
            type="teriyaki-sauce",
            imageLink="https://d3hvwccx09j84u.cloudfront.net/200,200/ingredient/64da2946d3fa192603728944-4fbfd649.png"
            ), 
        second_option=Ingredient(
            name="Sojasoße",
            type="soy-sauce",
            imageLink="https://d3hvwccx09j84u.cloudfront.net/200,200/ingredient/64da2921d3fa19260372871b-bf6f58c5.png"
            ),
        ),
]

@fastapi_app.get("/recommendations", response_model=list[Recipe])
async def recommendations(request: Request):
    user = request.headers.get("user")
    if user == None:
        return 400
    user_obj = get_preference_or_create(cast(str, user))
    recipes = all_recipes()
    return rank(user_obj, recipes)

@fastapi_app.get("/ingredients", response_model=list[Ingredient])
async def get_ingredients():
    return [
        Ingredient(name=i["name"], type=i["type"], imageLink=i["imageLink"],) for i in ingredients
    ]

@fastapi_app.post("/preferences/add", response_model=list[Recipe])
async def add_preferences(userPreferences: UserPreferenceUpdate):
    add_multiple_preferences(userPreferences)
    return recipes

@fastapi_app.get("/options", response_model=list[Option])
async def get_options():
    return options
    

