from django.shortcuts import render
from django.views import View
import requests
from .models import ConsultarRuc

# Create your views here.


def validar_ruc(ruc):
    url = f''
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
        