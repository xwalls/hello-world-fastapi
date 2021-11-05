from fastapi import FastAPI, Body, Query
from routers import users

app = FastAPI()
app.include_router(users.router)


@app.get("/")
def read_root():
    return {
        "message": "Welcome to the stream mariaffeet:!!",
        "url": "https://random-d.uk/api/131.jpg",
    }
