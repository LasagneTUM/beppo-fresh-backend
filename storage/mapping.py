from typing import List, Set
import json
from data.options import options

def collect_tags() -> Set[str]:
    with open("data/mockedRecipes.json", encoding="utf-8") as f:
        recipes = json.load(f)
        recipes = [i['recipe'] for i in recipes]
        tags_list = [i['tags'] for i in recipes]
        tags_list = [i for row in tags_list for i in row]
        tags_list = [i["name"] for i in tags_list]

        ingredients_list = [i['ingredients'] for i in recipes]
        ingredients_list = [i for row in ingredients_list for i in row]
        ingredients_list = [i["name"] for i in ingredients_list]

        allergens_list = [i['allergens'] for i in recipes]
        allergens_list = [i for row in allergens_list for i in row]
        allergens_list = [i["name"] for i in allergens_list]

        options_list = []

        for entry in options:
            options_list.append(entry.first_option.name)
            options_list.append(entry.second_option.name)
            

        return set(tags_list + ingredients_list + options_list + allergens_list)


vector_mapping_lst = collect_tags()

vector_mapping = {e:idx for idx, e in enumerate(vector_mapping_lst)}

def map_preference_to_idx(preference: str) -> int:
    return vector_mapping[preference]

def generate_empty_array() -> List[float]:
    return [0 for _ in vector_mapping.keys()]

def generate_array_for_taglist(tags: set[str]) -> List[float]:
    lst : List[float] = []
    for i in vector_mapping_lst:
        if i in tags:
            lst.append(10)
        else:
            lst.append(0)
    return lst