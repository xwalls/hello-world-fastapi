from fastapi import APIRouter, Body
from app.db import database
from app.models.user import User

router = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"description": "Not found"}}
)


@router.get("/")
def get_users():
    return database


@router.post("/create")
def create_user(user: User = Body(...)):
    database.append(user)
    return user


@router.put("/{user_id}/update")
def update_user(user_id: int, new_user: User = Body(...)):
    stored_user = database[user_id]
    update_data = new_user.dict(exclude_unset=True)
    updated_person = stored_person.copy(update=update_data)
    database[person_id] = updated_person
    return updated_person


@router.delete("/{person_id}")
def delete_person(person_id: int):
    database.pop(person_id)
    return database
