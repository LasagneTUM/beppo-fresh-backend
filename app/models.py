from pydantic import BaseModel

class UserPreference(BaseModel):
    user: str
    preference: str