from os import walk
import threading


import pandas as pd


class Process(object):
    
    BasePath: str
    
    def __init__(self,folder) -> None:
        self.BasePath = "./files/"+folder  + "/"
    
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
        dataframes= []
        for i in self.getFileNames():
            print('lendo '+i)
            dataframes.append(self.separate(i))
            print('terminou '+i)
        print('concatenando')
        self.empresas = pd.concat(dataframes, axis=1, ignore_index=False)
        print('concatenando terminou')
        print(self.empresas)

    def separate(self,nome_arquivo:str):
        return self.readFile(nome_arquivo, ['cnpj' ,'Nome Social' , 'naturezaJuridico',  'qualificacao',   'capital'  ,'porte' ,'responsavel'])
    
    def filtrar(self,dados:dict={},ou=False,nao=False,e=False):
        #for file in self.getFileNames():
        #for lista in self.readFile("K3241.K03200Y6.D20813.EMPRECSV"): 
            #all(x in lista for x in dados.keys())
        print(self.readFile("K3241.K03200Y6.D20813.EMPRECSV"))        
        

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
"""temos que ver como faz para q seja mais rapido pq ele ta lendo os arquivos e botando em um so mas ta demorando demais e n sei o q fazer
pensei em fazer uma clase multitreding para q cada uma leia um arquivo diferente mas o problema esta na juncao de todas, tem q juntar todas sai facilita tudo pq o 
panda ja tem coisa de filtros
"""

