from typing import Union, Dict, Any, Optional
import os
from dotenv import load_dotenv
load_dotenv()

from pymongo import MongoClient
from .mapping import map_preference_to_idx, generate_empty_array

db_client : MongoClient = MongoClient(f"mongodb+srv://nhuels:{os.getenv('MONGODB_PWD')}@cluster0.xnjrnzh.mongodb.net/?retryWrites=true&w=majority")

preference_collection = db_client.beppofresh.user
recipe_collection = db_client.beppofresh.recipes

def get_preference_or_create(user: str) -> Optional[Dict[str, Any]]:
    found = preference_collection.find_one({"name": user})
    if found == None:
        return create_new_user(user)
    else:
        return found

def add_preference(user: str, preference: str, pref_value: int):
    get_preference_or_create(user)
    preference_collection.update(
        {"name": user},
        {"$inc": {
            f"preferences.{str(map_preference_to_idx(preference))}": pref_value}}
    )

def create_new_user(user: str):
    content = {
            "name":user, "preferences": generate_empty_array()
        }
    preference_collection.instert_one(content)
    return content