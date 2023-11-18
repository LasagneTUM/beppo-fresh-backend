from typing import List
from pydantic import BaseModel

class PreferenceUpdate(BaseModel):
    preference: str
    preference_change: float

class UserPreferenceUpdate(BaseModel):
    user: str
    preference_updates: List[PreferenceUpdate]

class UserPreference(BaseModel):
    name: str
    preferences: List[float]

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
    vector: List[float]

class Ingredient(BaseModel):
    name: str
    type: str
    imageLink: str

class Option(BaseModel):
    first_option: Ingredient
    second_option: Ingredient