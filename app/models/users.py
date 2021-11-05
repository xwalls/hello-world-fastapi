from typing import Optional
from pydantic import BaseModel, Field, EmailStr

class User(BaseModel): 
    name: Optional[str] = None
    age: Optional[int] = None
    hair_color: Optional[str] = Field(
        None, 
        max_length=50,
        title="User's hair color",
        description="This is the User's hair color."
    )
    is_married: Optional[bool] = Field(
        None, 
        title="User's status",
        description="This is the User's status."
    )
    email: EmailStr = Field(
        title="User's email",
        description="This is the person's email."
    )
