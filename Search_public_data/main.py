from asyncore import read
import time
from unicodedata import name
from pandas import DataFrame
from re import  search
from os import walk
import threading
import pandas as pd
import tkinter as tk
from tkinter import font as tkFont  
class Process(object):
    
    BasePath: str
    campos:list
    info: DataFrame
    def __init__(self,folder,names) -> None:
        self.BasePath = "./files/"+folder
        self.campos = names
    
    def read(self):
        self.info = self.readFile('ALL',self.campos)
    def readFile(self, filename:str ,names:list[str]) -> list[dict[str:str]]:

        return pd.read_csv(self.BasePath + "/test",
                           sep=';',names=names, 
                           encoding='latin-1')
        # with open(self.BasePath + filename,encoding="latin-1") as f:
        #    return list(map(lambda x:x.strip().replace('"',"").split(';'),f.readlines(4)))
            
    def filtrar(self,dados:list[dict]=[],nao:dict={}):
        listaFiltrada = []
        newlista =[]
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
        super().__init__('EMPRESAS',['cnpj' ,'nomeSocial' , 'naturezaJuridico',
                        'qualificacao','capital','porte' ,'responsavel'])
        
    
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
        
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Whatzapp Bot')
        self.geometry("500x500")
        self.maxsize(500,500)
        
        tk.Button(self, text='Empresas',height= 3, width=10, command=lambda: self.comecar(Empresas()),font=tkFont.Font(family='Helvetica', size=10, weight='bold')).place(x=70, y=330)
        tk.Button(self, text='Socios',height= 3, width=10, command=lambda:self.comecar(Socios()),font=tkFont.Font(family='Helvetica', size=10, weight='bold')).place(x=350, y=330)
        tk.Button(self, text='Estabelecimentos',height= 4, width=14, command=lambda:self.comecar(Establecimentos()),font=tkFont.Font(family='Helvetica', size=8, weight='bold')).place(x=200, y=325) 
    def comecar(self,tipo):
        list = self.winfo_children()
        for l in list:
            l.destroy()
        
            
        tk.Label(self, text="Lendo Arquivo....",font=tkFont.Font(family='Helvetica', size=8, weight='bold')).place(x=150,y=220)
        tk.Label(self, text="Isso pode demorar um pouco",font=tkFont.Font(family='Helvetica', size=8, weight='bold')).place(x=150,y=240)  
        tipo.read()
        
        
        

                
t = time.process_time()      
if __name__ == "__main__":
    app = App()
    app.mainloop()

#do some stuff
elapsed_time = time.process_time() - t


print(elapsed_time)