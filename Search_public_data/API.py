#ignore o erro
import pandas as pd
from pandas.core.frame import DataFrame
from fastapi import FastAPI,Request

app = FastAPI()
names = ['cnpj' ,'nomeSocial' , 'naturezaJuridico',
                        'qualificacao','capital','porte' ,'responsavel']
data: DataFrame
data = pd.read_csv('./files/EMPRESAS/test',sep=';',names=names, encoding='latin-1')
print("read data complete")

@app.get("/")
async def read_root(request: Request):
    json_request = await request.json()
    if json_request["type"] == "empresas":
        del json_request["type"]
        empresas = []
        for i in json_request.keys():
            print(i)
        
        return {"empresas": empresas}
    if json_request["type"] == "socios":
        return  {"socios": ""}
    if json_request["type"] == "estabelecimentos":
        
        return  {"estabelecimentos": ""}
    
    return {"Erro Request": " Confirme se o body esta correto"}