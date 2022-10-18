import csv
import re
import sys
from datetime import date
from os import walk

from odf import teletype, text
from odf.opendocument import load

folder = sys.argv[1]
inicio = date(2017,1,1)
lista_dict_proyectos = []
lista_TIR = []
for nombreFichero in next(walk('\\'.join(__file__.split('\\')[:-1]) +"\\"+ folder), (None, None, []))[2] :
    textdoc = load(f"./{folder}/{nombreFichero}")
    allparas = textdoc.getElementsByType(text.P)

    resultado, year, month, day =  [int(x) for x in re.findall(r'\d+',teletype.extractText(allparas[-5]))]
    fecha_cierre = date(year,month,day)
    numero_dias = (fecha_cierre-inicio).days

    tir = (resultado/10000)**(365.25/numero_dias)
    lista_TIR.append(tir)
    
    lista_dict_proyectos.append({"nombre":nombreFichero[:-4],"resultado":resultado,"fecha de cierre":fecha_cierre,"numero dias": numero_dias,"TIR": tir})

with open(f'{folder}.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    for i in lista_dict_proyectos:
        writer.writerow(i.values())
    
    writer.writerow("")
    
    writer.writerow([f"Rentabilidad media: {sum(lista_TIR)/len(lista_TIR)}"])
    
    
    
    
    
    
    

    

    
    