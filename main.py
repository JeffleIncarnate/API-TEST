from typing import Optional
from fastapi import FastAPI
from Reader import read_json


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/api/readed")
async def return_data():
    return read_json()
