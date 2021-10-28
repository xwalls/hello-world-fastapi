from typing import Optional
from fastapi import FastAPI, Body, Query
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

#######################
# CLASSES

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


#######################
# DATABASE
database = [1]
persons_database = []

##################################################################
# ROOT PATH OPERATION
@app.get("/")
def read_root():
    return {"message": "Welcome to the stream Hypesor and Ramskat!!", "url":"https://random-d.uk/api/131.jpg"}

##################################################################
# CRUD (CREATE,READ,UPDATE,DELETE)
@app.get("/item")
def get_items():
    return database

@app.post("/item/{number}")
def create_item(number: int):
    database.append(number)
    return database

@app.put("/item/{number}")
def update_item(number: int, position: Optional[int] = -1):
    database[position] = number
    return database

@app.delete("/item")
def delete_item(position: Optional[int] = -1):
    database.pop(position)
    return database


##################################################################
# PERSONS CRUD

@app.get("/person/all")
def get_persons():
    return persons_database

# Request and Response Body
@app.post("/person/create")
def create_person(person: Person = Body(...)):
    persons_database.append(person)
    return person

# Validations: Query Parameters
@app.post("/person/details")
def details_person(
    name: str = Query(
        ..., 
        max_length=50,
        title="Person Name",
        description="This is the person's name.",
    ),
    age: int = Query(
        ..., 
        gt=1,
        lt=120,
        title="Person Age",
        description="This is the person's age.",
    )):

    return {name:age}

##################################################################
# Validations: Path Parameters

@app.get("/person/{person_id}")
def person_by_id(person_id: int):
    return persons_database[person_id]

@app.delete("/persons/{person_id}")
def delete_person(person_id: int):
    persons_database.pop(person_id)
    return persons_database

@app.put("/persons/{person_id}/update")
def update_person(person_id: int, new_person: Person = Body(...)):
    stored_person = persons_database[person_id]
    update_data = new_person.dict(exclude_unset=True)
    updated_person = stored_person.copy(update=update_data)
    persons_database[person_id] = updated_person

    return updated_person

##################################################################
# Validations: Models
# https://pydantic-docs.helpmanual.io/usage/schema/

##################################################################
# Special Data Types
# https://pydantic-docs.helpmanual.io/usage/types/#urls