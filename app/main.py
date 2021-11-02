from fastapi import FastAPI, Body, Query
from routers import persons

app = FastAPI()
app.include_router(persons.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the stream mariaffeet:!!", "url":"https://random-d.uk/api/131.jpg"}
