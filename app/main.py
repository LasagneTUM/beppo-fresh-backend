from typing import Union, List
import json

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from .models import UserPreference, Ingredient, Recipe, Option

from storage import add_preference

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
    return recipes

@fastapi_app.get("/ingredients", response_model=list[Ingredient])
async def get_ingredients():
    return [
        Ingredient(name=i["name"], type=i["type"], imageLink=i["imageLink"],) for i in ingredients
    ]

@fastapi_app.post("/preferences/add")
async def add_preferences(userPreference: UserPreference):
    add_preference(userPreference.user, userPreference.preference, userPreference.preference_change)
    return recipes

@fastapi_app.get("/options", response_model=list[Option])
async def get_options():
    return options
    

