import shutil
from os import walk
import pandas as pd
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
estabelecimentoSQL = ["cnpjBasico nvarchar(200) primary key,"]

for i in estabelecimentoSQL[1:-1]:
    estabelecimentoSQL.append(f"{i} nvarchar(200),")
estabelecimentoSQL.append("dataSituacaoEspecial nvarchar")

empresas =['cnpjBasico' ,'nomeSocial' , 'naturezaJuridico',
    'qualificacaoCodigo','capital','porte' ,'responsavel']

empresasSQL = ["cnpjBasico nvarchar(200) primary key,"]

for i in empresas[1:-1]:
        empresasSQL.append(f"{i} nvarchar(200),")
empresasSQL.append("responsavel nvarchar(200)")

socios = ['cnpjBasico',"identificadorSocio","nomeSociorazaoSocial",
    "cnpjcpfSocio","qualificacaoCodigo" ,'dataEntradaSociedade',
    'dataSituacaoCadastral', 'motivoSituacaoCadastral', "nomeCidadeExterior",
    "pais","represetante","nomeRepresentante",
    'qualificacoesRepresentante','faixaEtaria']

sociosSQL = ["cnpjBasico nvarchar(200) primary key,"]

for i in socios[1:-1]:
    sociosSQL.append(f"{i} varchar(200),")
sociosSQL.append("faixaEtaria varchar")

simples = ["cnpjBasico","opcaoSimples","dataOpcao","dataExclusao","opcaoMei","dataOpcaoMei","dataExclusaoMei"]
simplesSQL = ["cnpjBasico nvarchar(200) primary key,"]

for i in simples[1:-1]:
    simplesSQL.append(f"{i} varchar(200),")
simplesSQL.append("dataExclusaoMei varchar")

        

print("terminado parte1")
conn = mysql.connector.connect(host='localhost',
                                         database='public',
                                         user='root',
                                         password='225236')
print("feita conecao")
cursor = conn.cursor()
for chave,valor in {'cnae':"F.K03200$Z.D20910.CNAECSV",'municipio':"F.K03200$Z.D20910.MUNICCSV",'naturezaJuridico':"F.K03200$Z.D20910.NATJUCSV",
                    "pais":"F.K03200$Z.D20910.PAISCSV","qualificacao":"F.K03200$Z.D20910.QUALSCSV"}.items():
    try:cursor.execute(f'''
		CREATE TABLE {chave} (
			codigo nvarchar(50) primary key,
			descricao nvarchar(50)
			);
               ''')
    except:pass
    df = pd.read_csv("/".join(__file__.split("\\")[:-1])+ f"/files/atributos/"+ valor,sep=';',names =["codigo","descricao"], 
        encoding='latin-1')
    for row in df.itertuples():
        try:
            a= f"""INSERT INTO public.{chave.lower()} (codigo, descricao) VALUES ("{row.codigo}","{row.descricao}")"""
            cursor.execute(a)
        except:
            print

print("terminado atributos")
for chave,valor in {'EMPRESAS':["EMPRESASALL",empresasSQL,empresas],'ESTABELECIMENTOS':["ESTABELECIMENTOSALL",estabelecimentoSQL,estabelecimento],'SOCIOS':["SOCIOSALL",sociosSQL,socios],"SIMPLES":["SIMPLESALL",simplesSQL,simples]}.items():
    if chave == 'EMPRESAS':
        cursor.execute('USE public')
        try:
            cursor.execute(f"DROP TABLE {chave}")
        except:
            pass
        
        cursor.execute(f'''
        	    CREATE TABLE {chave} (
                {''.join(empresasSQL)}
        		);
                   ''')
        
        df = pd.read_csv("/".join(__file__.split("\\")[:-1])+ f"/files/{valor[0]}",sep=';',names =valor[2], 
            encoding='latin-1')
        print(df)
        for row in df.itertuples() :
                a= f"""INSERT INTO public.{chave.lower()} ({",".join(valor[2])}) VALUES ("{row.cnpjBasico}","{row.nomeSocial}","{row.naturezaJuridico}","{row.qualificacaoCodigo}","{row.capital}","{row.porte}","{row.responsavel}")"""
                cursor.execute(a)
                
        print("terminado atributos")
    if chave == 'SOCIOS':
        cursor.execute('USE public')
        try:
            cursor.execute(f"DROP TABLE {chave} ")
        except:
            pass
        try:
            cursor.execute(f'''
        	    CREATE TABLE {chave} (
                {''.join(empresasSQL)}
        		)
                
                   ''')
            
        except:
            pass
        df = pd.read_csv("/".join(__file__.split("\\")[:-1])+ f"/files/{valor[0]}",sep=';',names =valor[2], 
            encoding='latin-1')
        print(df)
        for row in df.itertuples() :
            try:
                a= f"""INSERT INTO public.{chave.lower()} ({",".join(valor[2])}) VALUES 
                ("{row.cnpjBasico}",
                "{row.identificadorSocio}",
                "{row.nomeSociorazaoSocial}",
                "{row.cnpjcpfSocio}","{row.qualificacaoCodigo}",
                "{row.dataEntradaSociedade}","{row.dataSituacaoCadastral}",
                "{row.motivoSituacaoCadastral}","{row.nomeCidadeExterior}","{row.pais}","{row.represetante}","{row.nomeRepresentante}","{row.qualificacoesRepresentante}","{row.faixaEtaria}")"""
                
                cursor.execute(a)
            except:
                pass
        print("terminado atributos")
    if chave == 'ESTABELECIMENTOS':
        cursor.execute('USE public')
        try:
            cursor.execute(f"DROP TABLE {chave}")
        except:
            pass
        try:
            cursor.execute(f'''
         	    CREATE TABLE {chave} (
                {''.join(empresasSQL)}
         		);
                   ''')
        except:
            pass
        df = pd.read_csv("/".join(__file__.split("\\")[:-1])+ f"/files/{valor[0]}",sep=';',names =valor[2], 
            encoding='latin-1',)
        for row in df.itertuples() :
            a= f"""INSERT INTO public.{chave.lower()} ({",".join(valor[2])}) VALUES 
            ("{row.cnpjBasico}",
            "{row.cpnjOrdem}",
            "{row.cnpjDv}",
            "{row.matriz}",
            "{row.nomeFantasia}",
            "{row.situacaoCadastral}","{row.dataSituacaoCadastral}",
            "{row.motivoSituacaoCadastral}","{row.nomeCidadeExterior}","{row.pais}","{row.dataAtividade}",
            "{row.cnaePrincipal}","{row.cnaeSecundario}","{row.tipoLogradouro}","{row.logradouro}",
            "{row.numero}",
            "{row.complemento}",
            "{row.bairro}","{row.cep}","{row.uf}","{row.municipio}","{row.ddd1}","{row.telefone1}","{row.ddd2}","{row.telefone2}","{row.dddFax}",
            "{row.fax}","{row.correioEletronico}","{row.situacaoEspecial}","{row.dataSituacaoEspecial}")"""

            cursor.execute(a)

            print("terminado estabelecimentos")
    if chave == "SIMPLES":
        cursor.execute('USE public')
        try:
            cursor.execute(f"DROP TABLE {chave};")
        except:
            pass
        try:
            cursor.execute(f'''
         	    CREATE TABLE {chave} (
                {''.join(simplesSQL)}
         		);
                   ''')
        except:
            pass
        df = pd.read_csv("/".join(__file__.split("\\")[:-1])+ f"/files/{valor[0]}",sep=';',names =valor[2], 
            encoding='latin-1',)
        print(df)
        for row in df.itertuples() :
            a= f"""INSERT INTO public.{chave.lower()} ({",".join(valor[2])}) VALUES 
            ("{row.cnpjBasico}",
            "{row.opcaoSimples}",
            "{row.dataOpcao}",
            "{row.dataExclusao}",
            "{row.opcaoMei}",
            "{row.dataOpcaoMei}","{row.dataExclusaoMei}")"""
    
            cursor.execute(a)
        print("terminado atributos")
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
    "cnpjcpfSocio","qualificacaoSocio" ,'dataEntradaSociedade',
    'dataSituacaoCadastral', 'motivoSituacaoCadastral', "nomeCidadeExterior",
    "pais","represetante","nomeRepresentante",
    'qualificacoesRepresentante','faixaEtaria'
"""
""" EMPRESAS
    'cnpj' ,'nomeSocial' , 'naturezaJuridico',
    'qualificacao','capital','porte' ,'responsavel'
"""