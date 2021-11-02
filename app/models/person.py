from typing import Optional
from pydantic import BaseModel, Field, EmailStr

class Person(BaseModel): 
    name: Optional[str] = None
    age: Optional[int] = None
    hair_color: Optional[str] = Field(
        None, 
        max_length=50,
        title="Person's hair color",
        description="This is the person's hair color."
    )
    is_married: Optional[bool] = Field(
        None, 
        title="person's status",
        description="This is the person's status."
    )
    email: EmailStr = Field(
        title="person's email",
        description="This is the person's email."
    )
