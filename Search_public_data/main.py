import time
from pandas import DataFrame
from re import  search
from os import walk
import threading
import pandas as pd

class Process(object):
    
    BasePath: str
    campos:list
    info: DataFrame
    def __init__(self,folder) -> None:
        self.BasePath = "./files/"+folder  
    
    def readFile(self, filename:str ,names:list[str]) -> list[dict[str:str]]:

        return pd.read_csv(self.BasePath+filename,
                           sep=';',names=names, 
                           encoding='latin-1')
        # with open(self.BasePath + filename,encoding="latin-1") as f:
        #    return list(map(lambda x:x.strip().replace('"',"").split(';'),f.readlines(4)))
            
    def filtrar(self,dados:list[dict]=[],nao:dict={}):
        listaFiltrada = []
        newlista =[]
        """
        for lista in self.info: 
            for i in dados:
                for chave in i.keys():
                   
                    
        return listaFiltrada"""
        for index,i in enumerate(dados):
            
            for chave in i.keys():
                for j in self.info[chave]:
                    
                    if search(i[chave],str(j)):
                        if chave in nao.keys():
                            
                            if not search(nao[chave],j):
                                listaFiltrada.append(index) 
                        else:
                            listaFiltrada.append(index)
        
        for i in listaFiltrada:
            newlista.append(self.info.iloc[i])
            
            
        return newlista
                        
    def getFileNames(self) -> list[str]:
        return next(walk(self.BasePath), (None, None, []))[2]
    
    
    
class Empresas(Process):
    
    info:DataFrame
    
    def __init__(self) -> None:
        super().__init__('EMPRESAS')
        self.campos = ['cnpj' ,'nomeSocial' , 'naturezaJuridico',
                        'qualificacao','capital','porte' ,'responsavel']
        self.info = self.separate('ALL')
        
        print(self.filtrar([{'cnpj':'41273602'},{'cnpj':'41273601'}]))
        

    def separate(self,nome_arquivo:str):
        return self.readFile(nome_arquivo, self.campos)
    
class Establecimentos(Process,threading.Thread):
    def __init__(self) -> None:
        super().__init__('ESTABELECIMENTO')
        self.campos = [
                    'cnpjBasico',"cpnjOrdem","cnpjDv",
                    "matriz","nomeFantasia" ,'situacaoCadastral',
                    'dataSituacaoCadastral', 'motivoSituacaoCadastral', "nomeCidadeExterior",
                    "pais","dataAtividade","cnaePrincipal",
                    'cnaeSecundario','tipoLogradouro' ,'logradouro',
                    "numero","complemento","bairro",
                    "cep","uf","municipio",
                    "ddd1","telefone1","ddd2",
                    "telefone2","dddFax","fax",
                    "correioEletronico","situacaoEspecial","dataSituacaoEspecial"]
        
        
    def separate(self,nome_arquivo:str):
        return self.readFile(nome_arquivo,self.campos)

class Socios(Process,threading.Thread):
    def __init__(self) -> None:
        super().__init__('SOCIOS')
        self.campos =  ['cnpjBasico',"identificadorSocio","nomeSocio-razaoSocial",
                        "cnpj-cpfSocio","qualificacaoSocio" ,'dataEntradaSociedade',
                        'dataSituacaoCadastral', 'motivoSituacaoCadastral', "nomeCidadeExterior",
                        "pais","represetante","nomeRepresentante",
                        'qualificacoesRepresentante','faixaEtaria']
        
    def separate(self,nome_arquivo:str):
        return self.readFile(nome_arquivo,self.campos)

class start(object):
    empresas : Empresas
    establecimentos: Establecimentos
    socios: Socios
  
    def __init__(self) -> None:
        self.socios = Socios()
        self.empresas = Empresas()
        self.establecimentos = Establecimentos()
        
    def Startinput(self):
        tipo = {
            "socio" : 0,
            "estabelecimento" : 1,
            "empresa":2
            }
        datos = {}
        tipo = [self.socios,self.establecimentos,self.empresas][tipo[input("Que tipo buscar:Socio/Estabelecimento/Empresa").lower()]]
        for i in tipo.campos:
            datos[i] = input(f"digite {i}: ")
        tipo.filtrar("",datos)
        
        
                
t = time.process_time()      
start()

#do some stuff
elapsed_time = time.process_time() - t


print(elapsed_time)