from typing import List, Union
from pydantic import BaseModel

class PreferenceUpdate(BaseModel):
    preference: str
    preference_change: float

class UserPreferenceUpdate(BaseModel):
    user: str
    preference_updates: List[PreferenceUpdate]

class UserPreference(BaseModel):
    name: Union[str,None]
    preferences: List[float]

class TagEntry(BaseModel):
    name: str

class IngredientEntry(BaseModel):
    name: str
    imageLink: str

class AllergeenEntry(BaseModel):
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
    allergeens: List[AllergeenEntry]
    ingredients: List[IngredientEntry]
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