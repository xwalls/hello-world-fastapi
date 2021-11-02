from fastapi import APIRouter, Body
from db import database
from models.person import Person

router = APIRouter(
    prefix="/persons",
    tags=["persons"],
    responses={404: {"description": "Not found"}})

@router.get("/")
def get_persons():
    return database

@router.post("/create")
def create_person(person: Person = Body(...)):
    database.append(person)
    return person

@router.put("/{person_id}/update")
def update_person(person_id: int, new_person: Person = Body(...)):
    stored_person = database[person_id]
    update_data = new_person.dict(exclude_unset=True)
    updated_person = stored_person.copy(update=update_data)
    database[person_id] = updated_person
    return updated_person

@router.delete("/{person_id}")
def delete_person(person_id: int):
    database.pop(person_id)
    return database
