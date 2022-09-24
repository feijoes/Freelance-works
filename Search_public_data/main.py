
from operator import index
import time
from pandas import DataFrame
from re import  search
from os import walk
import threading
import pandas as pd
import tkinter as tk
import itertools

from tkinter import font as tkFont,Entry


class Process(object):

    BasePath: str
    campos:list
    info: DataFrame
    def __init__(self,folder,names) -> None:
        self.BasePath = "./files/"+folder
        self.campos = names
    def read(self):
        self.info = self.readFile('ALL',self.campos)
    async def readFile(self, filename:str ,names:list[str]) -> list[dict[str:str]]:
        return pd.read_csv(self.BasePath+'/EMPRESAS'+filename,sep=';',names=names, encoding='latin-1')
    def filtrar(self,dados:list[dict]=[],nao:list[dict]=[]):
        print(dados,nao)
        listaFiltrada = []
        for i in dados:
           for chave in i.keys():
               for index,j in enumerate(self.info[chave]):  
                   if search(i[chave],str(j)):
                       if chave in [*itertools.chain.from_iterable(nao)]:
                            if not search(nao[chave],j):
                               listaFiltrada.append(index) 
                       else:
                           listaFiltrada.append(index)
        newlista = [self.info.iloc[i] for i in listaFiltrada]
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
        self.dados = []
        super().__init__()
        self.title('Whatzapp Bot')
        self.geometry("500x500")
        self.maxsize(500,500)
        
        tk.Button(self, text='Empresas',height= 3, width=10, command=lambda: self.comecar(Empresas()),font=tkFont.Font(family='Helvetica', size=10, weight='bold')).place(x=70, y=330)
        tk.Button(self, text='Socios',height= 3, width=10, command=lambda:self.comecar(Socios()),font=tkFont.Font(family='Helvetica', size=10, weight='bold')).place(x=350, y=330)
        tk.Button(self, text='Estabelecimentos',height= 4, width=14, command=lambda:self.comecar(Establecimentos()),font=tkFont.Font(family='Helvetica', size=8, weight='bold')).place(x=200, y=325) 
    
    def GetDados(self,children,campos,var):
        dado={}
        for i in range(len(campos)):
            dado[campos[i]] = children[i].get()
            children[i].delete(0, tk.END)
        
        dado["nao"] = var.get() == 1
        return dado
    
    def finalizar(self,campos,var,tipo):
        self.dados.append(self.GetDados([self.children[i] for i in self.children if "entry" in i],campos,var))
        self.apagar()
        campos.append('nao')
        for c,i in enumerate(campos):
            
            cell = Entry(self, width=10)
            cell.grid(row=0, column=c)
            cell.insert(0,f'{i}')
        dados = []
        for r,i in enumerate(self.dados):
            row = {}
            for (c,j) in enumerate(i.values()):
                row[campos[c]] = j
                cell = Entry(self, width=10)
                cell.grid(row=r+1, column=c)
                cell.insert(0,f'{j}' or "X")
            dados.append(row)
        tk.Button(self, text='Novo dados?',height= 2, width=14,   
                font=tkFont.Font(family='Helvetica', size=8, weight='bold')).place(x=0,y=r*20+40)
        tk.Button(self, text='Confirmar',height= 2, width=14, command=lambda:self.buscar(dados,tipo),   
                font=tkFont.Font(family='Helvetica', size=8, weight='bold')).place(x=110,y=r*20+40) 
    
    def buscar(self,dados,tipo):
       self.apagar()
       tipo.filtrar([{key : val for key, val in sub.items() if key != "nao" and val} for sub in dados if not sub["nao"]],
                          [{key : val for key, val in sub.items() if key != "nao" and val} for sub in dados if sub["nao"]])
       
        
                
            
    def Dados(self,tipo):
        
        x = 50
        y = 100
        var = tk.IntVar()
        tk.Checkbutton(self,text="Nao",variable=var).place(x=400,y=50)
        for i in tipo.campos:
            tk.Label(self, text=i.upper(),font=tkFont.Font(family='Helvetica', size=9, weight='bold')).place(x=x,y=y)
            tk.Entry(self,width=20).place(x=x,y=y+20)
            if x >= 250:
                y+=100
                x = 50
            else:
                x += 130
        tk.Button(self, text='Novo dados?',height= 2, width=14, 
                  command=lambda:self.dados.append(self.GetDados([self.children[i] for i in self.children if "entry" in i],tipo.campos,var)),
                  font=tkFont.Font(family='Helvetica', size=8, weight='bold')).place(x=400, y=325) 
        
        tk.Button(self,text='finalizar',height=2,width=10,
                  command=lambda:self.finalizar(tipo.campos,var,tipo),
                  font=tkFont.Font(family='Helvetica', size=8, weight='bold')).place(x=300, y=325) 
        
            
        
              
    
    def comecar(self,tipo):
        self.apagar()
        
            
        tk.Label(self, text="Lendo Arquivo....",font=tkFont.Font(family='Helvetica', size=8, weight='bold')).place(x=150,y=220)
        tk.Label(self, text="Isso pode demorar um pouco",font=tkFont.Font(family='Helvetica', size=8, weight='bold')).place(x=150,y=240) 
        
        tipo.read()
        self.apagar()
        
        tk.Label(self, text="Arquivo lido",font=tkFont.Font(family='Helvetica', size=8, weight='bold')).place(x=200,y=0)
        self.Dados(tipo)
        
    def apagar(self):
        list = self.winfo_children()
        for l in list:
            l.destroy()
   
t = time.process_time()      
if __name__ == "__main__":
    app = App()
    app.mainloop()

#do some stuff
elapsed_time = time.process_time() - t


print(elapsed_time)