from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    text: str
    date: str
app = FastAPI()


@app.post("/")
def create_item(item: Item):
    print(item)
    return item