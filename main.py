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

import uvicorn

if __name__ == "__main__":
  uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)