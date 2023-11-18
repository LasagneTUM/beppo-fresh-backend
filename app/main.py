from typing import Union, List, cast
import json

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from models.models import UserPreferenceUpdate, Ingredient, Recipe, Option

from storage import add_multiple_preferences, get_preference_or_create, all_recipes, save_recipe_data, recipe_collection, preference_collection

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

options = [
    Option(
        first_option=Ingredient(
            name="Chicken",
            type="meat",
            imageLink="https://www.aldelis.com/wp-content/uploads/2017/10/beneficios-pollo.jpg"
            ), 
        second_option=Ingredient(
            name="Tofu",
            type="tofu",
            imageLink="https://www.fitforfun.de/files/images/201706/1/geschnittener-tofu-in-schuessel,251508_1x1_xl.jpg"
            ),
        ),
    Option(
        first_option=Ingredient(
            name="Indian",
            type="exotic",
            imageLink="https://i.etsystatic.com/33245026/r/il/1f9336/3612599268/il_570xN.3612599268_ccik.jpg"
            ), 
        second_option=Ingredient(
            name="Thai",
            type="exotic",
            imageLink="https://i.etsystatic.com/33245026/r/il/f13729/3660574045/il_570xN.3660574045_2s5z.jpg"
            ),
        ),
    Option(
        first_option=Ingredient(
            name="Spicy",
            type="exotic",
            imageLink="https://www.google.de/url?sa=i&url=https%3A%2F%2Fwww.popularmechanics.com%2Fscience%2Fhealth%2Fa45140555%2Fone-chip-challenge-spicy-food-danger%2F&psig=AOvVaw2Xq6pjg1OqRO05AaE-tF1M&ust=1700419800989000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCMD8vsmbzoIDFQAAAAAdAAAAABAD"
            ), 
        second_option=Ingredient(
            name="Not spicy",
            type="not exotic",
            imageLink="https://cdn3.iconfinder.com/data/icons/food-grade-2/29/food-grade-mild-512.png"
            ),
        ),
    Option(
        first_option=Ingredient(
            name="Mushroom",
            type="mushroom",
            imageLink="https://hips.hearstapps.com/hmg-prod/images/types-of-mushrooms-1644507973.jpeg?crop=0.668xw:1.00xh;0.112xw,0&resize=640:*"
            ), 
        second_option=Ingredient(
            name="Salad",
            type="healthy",
            imageLink="https://hellolittlehome.com/wp-content/uploads/2022/08/garden-salad-recipe-2.jpg"
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
    

