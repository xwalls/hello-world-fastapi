from typing import Optional
from fastapi import FastAPI

app = FastAPI()

database = [1]

@app.get("/api/quack")
def read_root():
    return {"message": "Hello Hypesor!", "url":"https://random-d.uk/api/131.jpg"}

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