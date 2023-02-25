import requests
from django.conf import settings 
import json

def conseguir_TOKEN(client_id,client_secret):
    URL = f"https://api-seguridad.sunat.gob.pe/v1/clientesextranet/{client_id}/oauth2/token/"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
    json = {
        "grant_type": "client_credentials",
        "scope" :"https://api.sunat.gob.pe/v1/contribuyente/contribuyentes",
        "client_id" :client_id ,
        "client_secret" :client_secret,
    }
    response = requests.post(URL,data=json,headers=headers)
    return response.json()["access_token"]

def validar_ruc(data : dict[str,any]) -> dict[str:any]:
    url = f'https://api.sunat.gob.pe/v1/contribuyente/contribuyentes/{data["numRuc"]}/validarcomprobante'

    headers : dict[str:str] = {
        "Authorization" : "Bearer "+ conseguir_TOKEN( settings.CLIENT_ID,settings.CLIENT_SECRET)
    }

    body : dict[str: any] = dict(data.items())
    
    if not body["monto"]: del body["monto"]
    del body["csrfmiddlewaretoken"]
        

    response = requests.post(url,json=body,headers=headers)
    print(response.content)
    return response.json()

def validar_numero_ruc(n_ruc)-> list[bool,dict[str:any]]:
    URL = f"https://api.apis.net.pe/v1/ruc?numero={n_ruc}"
    
    JSON = requests.get(url=URL)
    response: dict[str:any] = JSON.json()
    if response.get("error",None):
        return [False, response]
    return [True,response]

