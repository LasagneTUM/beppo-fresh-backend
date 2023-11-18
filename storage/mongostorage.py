from typing import Union, Dict, Any, Optional, List
import os
from dotenv import load_dotenv
load_dotenv()

from pymongo import MongoClient
from .mapping import map_preference_to_idx, generate_empty_array, generate_array_for_taglist

from models.models import UserPreferenceUpdate, Recipe, UserPreference

db_client : MongoClient = MongoClient(os.getenv("MONGODB_CONNECTION"))

preference_collection = db_client.beppofresh.user
recipe_collection = db_client.beppofresh.recipes

def get_preference_or_create(user: str) -> UserPreference:
    found = preference_collection.find_one({"name": user})
    if found == None:
        found =  create_new_user(user)
    return UserPreference.model_validate(found)
    
def add_multiple_preferences(userPreference: UserPreferenceUpdate):
    get_preference_or_create(userPreference.user)
    unpacked = [(update.preference, update.preference_change) for update in userPreference.preference_updates]
    inc_instruction = {
        f"preferences.{str(map_preference_to_idx(preference))}": pref_value for (preference, pref_value) in unpacked
        }

    preference_collection.update(
        {"name": userPreference.user},
        {"$inc": inc_instruction}
    )

def create_new_user(user: str) -> Dict[str, Any]:
    content = {
            "name":user, "preferences": generate_empty_array()
        }
    preference_collection.insert_one(content)
    return content

def save_recipe_data(recipe_data: List[Dict]):
    for recipe in recipe_data:
        vector = generate_array_for_taglist([t["name"] for t in recipe["tags"]])
        recipe['vector'] = vector
    recipe_collection.insert_many(recipe_data)

def all_recipes() -> List[Recipe]:
    return [Recipe.model_validate(r) for r in recipe_collection.find()]

def get_recipe_by_id(id: str) -> Recipe:
    return Recipe.model_validate(recipe_collection.find_one({"_id": id}))