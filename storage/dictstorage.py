from typing import Dict, Any, Set, Union

user_preferences: Dict[str, Set[str]] = {}

def add_preference(user: str, preference: str):
    if user not in user_preferences:
        user_preferences[user] = set([preference])
    else:
        user_preferences[user].add(preference)

def remove_preference(user: str, preference: str):
    if user not in user_preferences:
        return
    if preference in user_preferences[user]:
        user_preferences[user].remove(preference)

def get_preference(user: Union[str,None]) -> Set[str]:
    if user in user_preferences:
        return user_preferences[user]
    return set()