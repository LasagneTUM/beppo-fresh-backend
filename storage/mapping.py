from typing import List

vector_mapping_lst = [
    "pizza",
    "pasta",
    "pesto",
    "burrito",
    "cheese",
    "tomatoes",
    "zucchini",
    "eggplant",
    "eggs",
    "italian",
    "mushrooms",
    "chicken",
    "beef",
    "pork",
    "fish"
]

vector_mapping = {e:idx for idx, e in enumerate(vector_mapping_lst)}

def map_preference_to_idx(preference: str) -> int:
    return vector_mapping[preference]

def generate_empty_array() -> List[float]:
    return [0 for _ in vector_mapping.keys()]

def generate_array_for_taglist(tags: List[str]) -> List[float]:
    lst : List[float] = []
    for i in vector_mapping_lst:
        if i in tags:
            lst.append(10)
        else:
            lst.append(0)
    return lst