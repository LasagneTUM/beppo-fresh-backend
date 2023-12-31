from typing import List, Tuple

from models.models import UserPreference, Recipe

from sklearn.metrics.pairwise import cosine_similarity

def calculate_score(lst1: List[List[float]], lst2: List[List[float]]) -> float:
    return cosine_similarity(lst1, lst2)[0][0]

def rank(user: UserPreference, recipes: List[Recipe]) -> List[Recipe]:
    ranked : List[Tuple[Recipe, float]] = []
    for r in recipes:
        ranked.append((r, calculate_score(
            [user.preferences], 
            [r.vector])
            ))
    ranked.sort(key=lambda x: x[1], reverse=True)
    return [r[0] for r in ranked]
