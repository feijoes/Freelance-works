from operator import truediv
from os import walk
import threading


import pandas as pd


class Process(object):
    
    BasePath: str
    
    def __init__(self,folder) -> None:
        self.BasePath = "./files/"+folder  
    
    def readFile(self, filename:str ,names:list[str]) -> list[dict[str:str]]:

        return pd.read_csv(self.BasePath + filename ,
                           sep=';',names=names, 
                           encoding='latin-1')
        with open(self.BasePath + filename,encoding="latin-1") as f:
            return list(map(lambda x:x.strip().replace('"',"").split(';'),f.readlines(4)))
            
    
    def getFileNames(self) -> list[str]:
        return next(walk(self.BasePath), (None, None, []))[2]
    
class Empresas(Process):
    
    empresas:list
   
    def __init__(self) -> None:
        super().__init__('EMPRESAS')
        self.empresas = self.separate('ALL')
        print(self.empresas.head())

    def separate(self,nome_arquivo:str):
        return self.readFile(nome_arquivo, ['cnpj' ,'Nome Social' , 'naturezaJuridico',  'qualificacao',   'capital'  ,'porte' ,'responsavel'])
    
    def filtrar(self,dados:list[dict]=[],nao:dict={}):
        listaFiltrada = []
        for lista in self.readFile("./files/EMPRESASALL"): 
            for i in dados:
                if all(x in lista for x in i.values()):
                    if all(not x in lista for x in nao.values()):
                        listaFiltrada.append(lista)
        return listaFiltrada
             
        

class Establecimentos(Process,threading.Thread):
    def __init__(self) -> None:
        super().__init__('ESTABELECIMENTO')


class Socios(Process,threading.Thread):
    def __init__(self) -> None:
        super().__init__('SOCIOS') 

class start(object):
    empresas : Empresas
    establecimentos: Establecimentos
    socios: Socios
    
    def __init__(self) -> None:
        self.socios = Socios()
        self.empresas = Empresas()
        self.establecimentos = Establecimentos()
start()


