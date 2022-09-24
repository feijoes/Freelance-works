from typing import Union
#ignore o erro
from fastapi import FastAPI

app = FastAPI()


@app.post("/")
async def read_root():
    return {"Hello": "World"}