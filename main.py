from typing import Optional
from fastapi import FastAPI
import Reader

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/api/readed")
async def return_data():
    return Reader.read_json()
