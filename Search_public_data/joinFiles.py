import shutil
from os import walk
import pyodbc
import pandas as pd
from sqlalchemy import create_engine

import mysql.connector

""" 
Arquivo python para leer todos os arquivos em uma pasta e juntar todos em 1 arquivo

como usar:
    python joinFiles.py NomeDaPasta LocalDoNovoArquivo+NomeArquivo
exemplo:
    python joinFiles.py EMPRESAS todasEmpresas
    
ira buscar os arquivos na pasta ./files/EMPRESAS/ e criara o arquivo em ./files/todasEmpresas
    
A pasta com os arquivos tem que estar dentro de ./files/
E o arquivo criado estara dentro de ./files/

depois ira traduzilos
joinfiles(f"./files/{sys.argv[1]}/",f"./files/{sys.argv[2]}")
Em caso que queira modificar a localizacao da pasta ou onde arquivo é salvo so mudar a linha abaixo
"""

def joinfiles(BasePath,filename):
    with open(filename,'wb') as wfd:
        for f in next(walk(BasePath), (None, None, []))[2]:
            with open(BasePath + f,'rb') as fd:
                shutil.copyfileobj(fd, wfd)
             
def get():
    
    
    path = './files/atributos/'
    lista =[]
    count = 0
    for f in next(walk(path), (None, None, []))[2]:
        info= pd.read_csv(path + f,sep=';',names =["num","atributo"], 
        encoding='latin-1',header=None)
        lista.append({ arquivos[count]:info })
        count += 1
        info.to_sql
    return lista
        
def atributo(a,num):
    return a.loc[a['num'] == num]['atributo'][1]

def seila(path,names):
    for f in next(walk(path), (None, None, []))[2]:
        info= pd.read_csv(path + f,sep=';',names =names, 
        encoding='latin-1')
        


arquivos = ['cnae','municipio','naturezaJuridico',"pais","qualificacao"]

estabelecimento = ['cnpjBasico',"cpnjOrdem","cnpjDv",
    "matriz","nomeFantasia" ,'situacaoCadastral',
    'dataSituacaoCadastral', 'motivoSituacaoCadastral', "nomeCidadeExterior",
    "pais","dataAtividade","cnaePrincipal",
    'cnaeSecundario','tipoLogradouro' ,'logradouro',
    "numero","complemento","bairro",
    "cep","uf","municipio",
    "ddd1","telefone1","ddd2",
    "telefone2","dddFax","fax",
    "correioEletronico","situacaoEspecial","dataSituacaoEspecial" ]

estabelecimentoSQL =[]
for i in estabelecimento:
    if i in arquivos:estabelecimentoSQL.append(f"FOREIGN KEY ({i}) REFERENCES {i}(codigo),")
    else: 
        if i == estabelecimento[-1]:estabelecimentoSQL.append(f"{i} nvarchar(266)")   
        else: estabelecimento.append(f"{i} nvarchar(266),")   

empresas =['cnpj' ,'nomeSocial' , 'naturezaJuridico',
    'qualificacao','capital','porte' ,'responsavel']

empresasSQL = []
for i in empresas:
    if i in arquivos:empresasSQL.append(f"FOREIGN KEY ({i}) REFERENCES {i}(codigo),")
    else: 
        if i == empresas[-1]:empresasSQL.append(f"{i} nvarchar(266)")   
        else: empresas.append(f"{i} nvarchar(266),")   


socios = ['cnpjBasico',"identificadorSocio","nomeSocio-razaoSocial",
    "cnpj-cpfSocio","qualificacaoSocio" ,'dataEntradaSociedade',
    'dataSituacaoCadastral', 'motivoSituacaoCadastral', "nomeCidadeExterior",
    "pais","represetante","nomeRepresentante",
    'qualificacoesRepresentante','faixaEtaria']


sociosSQL =[]
for i in socios:
    if i in arquivos:sociosSQL.append(f"FOREIGN KEY ({i}) REFERENCES {i}(codigo),")
    else: 
        if i == socios[-1]:sociosSQL.append(f"{i} nvarchar(266)")   
        else: sociosSQL.append(f"{i} nvarchar(266),")   
        
print("terminado parte1")
conn = mysql.connector.connect(host='localhost',
                                         database='public',
                                         user='root',
                                         password='225236')
print("feita conecao")
cursor = conn.cursor()


for chave,valor in {'cnae':"F.K03200$Z.D20910.CNAECSV",'municipio':"F.K03200$Z.D20910.MUNICCSV",'naturezaJuridico':"F.K03200$Z.D20910.NATJUCSV",
                    "pais":"F.K03200$Z.D20910.PAISCSV","qualificacao":"F.K03200$Z.D20910.QUALSCSV"}.items():
    
    cursor.execute(f'''
		CREATE TABLE {chave} (
			codigo nvarchar(10) primary key,
   
			descricao nvarchar(266)
			);
               ''')
    df = pd.read_csv("./info/atributos/" + valor,sep=';',names =["num","atributo"], 
        encoding='latin-1')
    df.to_sql(f'{chave}', con=conn)


print("terminado atributos")
for chave, valor in {"ESTABELECIMENTOS": estabelecimentoSQL, "SOCIOS":sociosSQL, "EMPRESAS":empresasSQL}.items():
    
    cursor.execute(f'''
		CREATE TABLE {chave} (
			int primary key,
   
            {"".join(valor)}
            
			);
               ''')


for i in {"ESTABELECIMENTOS": estabelecimentoSQL, "SOCIOS":sociosSQL, "EMPRESAS":empresasSQL}.keys():
    
    """AQUI SO PRECISA LEER PELO MENOS 1 EMPRESa , 1 SOCIO e 1 Estabelecimento """
    df = pd.read_csv("./ijdjhdfichsdichn" + valor,sep=';',names =names, 
        encoding='latin-1')
    df.to_sql(f'{chave}', con=conn)
""" 
empresasArquivos = ["naturezaJuridico","qualificacao"]
    establecimentosArquivos = ["cnae","municipio","pais"]
    sociosArquivos = ["pais","qualificacao"]
    
ESTABELECIMENTOS
    'cnpjBasico',"cpnjOrdem","cnpjDv",
    "matriz","nomeFantasia" ,'situacaoCadastral',
    'dataSituacaoCadastral', 'motivoSituacaoCadastral', "nomeCidadeExterior",
    "pais","dataAtividade","cnaePrincipal",
    'cnaeSecundario','tipoLogradouro' ,'logradouro',
    "numero","complemento","bairro",
    "cep","uf","municipio",
    "ddd1","telefone1","ddd2",
    "telefone2","dddFax","fax",
    "correioEletronico","situacaoEspecial","dataSituacaoEspecial" 
"""
""" SOCIOS
    'cnpjBasico',"identificadorSocio","nomeSocio-razaoSocial",
    "cnpj-cpfSocio","qualificacaoSocio" ,'dataEntradaSociedade',
    'dataSituacaoCadastral', 'motivoSituacaoCadastral', "nomeCidadeExterior",
    "pais","represetante","nomeRepresentante",
    'qualificacoesRepresentante','faixaEtaria'
"""
""" EMPRESAS
    'cnpj' ,'nomeSocial' , 'naturezaJuridico',
    'qualificacao','capital','porte' ,'responsavel'
"""