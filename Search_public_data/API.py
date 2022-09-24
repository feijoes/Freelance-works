from typing import Union
#ignore o erro
from fastapi import FastAPI

app = FastAPI()
with open("./files/EMPRESAS/test") as f:
    a = f.readlines()

@app.get("/")
async def read_root():
    print(a)
    return {"Hello": "World"}