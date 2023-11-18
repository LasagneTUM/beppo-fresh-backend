from typing import Union, Dict, Any, Optional

from pymongo import MongoClient
from .mapping import map_preference_to_idx, generate_empty_array

db_client : MongoClient = MongoClient("mongodb://localhost:27017/")

preference_collection = db_client.beppofresh.user
recipe_collection = db_client.beppofresh.recipes

def get_preference(user: Union[str,None]) -> Optional[Dict[str, Any]]:
    return preference_collection.find_one({"name": user})

def add_preference(user: str, preference: str, pref_value: int):
    found_user =  get_preference(user)
    if found_user != None:
        preference_collection.update(
            {"name": user},
            {"$inc": {
                f"preferences.{str(map_preference_to_idx(preference))}": pref_value}}
        )
    else:
        preference_collection.instert_one({
            "name":user, "preferences": generate_empty_array()
        })
