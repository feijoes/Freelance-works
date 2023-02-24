
from django.shortcuts import render
import requests
from django.core.handlers.wsgi import WSGIRequest
from django.conf import settings 
from .forms import VericarRucForm

def index(request: WSGIRequest):

    
    if request.method == "POST":
        new_Verificar = VericarRucForm(request.POST)
        
        if new_Verificar.is_valid():	
            new_Verificar.save()

    form = VericarRucForm() 
    return render(request, "validarRuc.html",{'form':form})


def validar_ruc(data : dict[str,any]):
    url = f'https://api.sunat.gob.pe/v1/contribuyente/contribuyentes/{data["numRuc"]}/validarcomprobante'

    headers : dict[str:str] = {
        "Authorization" : "Bearer "+ settings.TOKEN  
    } 

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Aquí puedes realizar las operaciones necesarias con la información obtenida
        # Por ejemplo, podrías devolver un diccionario con los datos relevantes
        return {
            'razon_social': data['razonSocial'],
            'direccion': data['direccion']
        }
    else:
        # Manejo de error en caso la API no responda correctamente
        print('Error en la consulta de RUC')
        