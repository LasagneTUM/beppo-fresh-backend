from typing import List
from pydantic import BaseModel

class UserPreference(BaseModel):
    user: str
    preference: str

class TagEntry(BaseModel):
    name: str

class NutritionInfo(BaseModel):
    energy: int
    calories: int
    carbohydrate: float
    protein: float

class Recipe(BaseModel):
    id: str
    name: str
    headline: str
    prepTime: int
    image: str
    websiteURL: str
    tags: List[TagEntry]
    nutrition: NutritionInfo

class Ingredient(BaseModel):
    name: str
    type: str
    imageLink: str

class Option(BaseModel):
    first_option: Ingredient
    second_option: Ingredient