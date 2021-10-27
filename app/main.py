from typing import Optional
from fastapi import FastAPI, Body, Query
from pydantic import BaseModel

app = FastAPI()

#######################
# Classes

class Person(BaseModel): 
    name: str
    age: int 
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


#######################
# DATABASE
database = [1]

##################################################################
# ROOT PATH OPERATION
@app.get("/")
def read_root():
    return {"message": "Hello xxxxxxx!", "url":"https://random-d.uk/api/131.jpg"}

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
# Request and Response Body
@app.post("/person/create")
def create_person(person: Person = Body(...)):
    return person

# Validations: Query Parameters
@app.post("/person/create")
def create_person(
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
