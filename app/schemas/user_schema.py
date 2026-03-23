from pydantic import BaseModel, Field
from typing import Optional


# Create User Schema
class UserCreate(BaseModel):

    username: str = Field(..., min_length=3, max_length=20)
    diary: str = Field(..., min_length=3)


# Response Schema
class UserResponse(BaseModel):

    id: str
    username: str
    diary: str


# Update Schema
class UserUpdate(BaseModel):

    username: Optional[str] = None
    diary: Optional[str] = None