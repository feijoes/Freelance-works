import shutil
from os import walk

import mysql.connector
import pandas as pd

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

for chave in ["EMPRESAS","ESTABELECIMENTOS","SOCIOS",'SIMPLES']:
    with open(chave+"ALL",'wb') as wfd:
         
        for f in next(walk(f"./files/{chave}/"), (None, None, []))[2]:
          
            with open(f"./files/{chave}/{f}",'rb') as fd:
                shutil.copyfileobj(fd, wfd)

            
estabelecimento = ['cnpjBasico',"cnpjOrdem","cnpjDv",
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

for i in estabelecimento[1:-1]:
    estabelecimentoSQL.append(f"{i} nvarchar(200),")
estabelecimentoSQL.append("dataSituacaoEspecial nvarchar(200)")

empresas =['cnpjBasico' ,'nomeSocial' , 'naturezaJuridico',
    'qualificacaoCodigo','capital','porte' ,'responsavel']

empresasSQL = ["cnpjBasico nvarchar(200) primary key,"]

for i in empresas[1:-1]:
        empresasSQL.append(f"{i} nvarchar(200),")
empresasSQL.append("responsavel nvarchar(200)")

socios = ['cnpjBasico',"identificadorSocio","nomeSociorazaoSocial",
    "cnpjcpfSocio","qualificacaoCodigoSocio" ,'dataEntradaSociedade',
    "paisSocio","represetante","nomeRepresentante",
    'qualificacoesRepresentante','faixaEtaria']

sociosSQL = ["cnpjBasico nvarchar(200) primary key,"]

for i in socios[1:-1]:
    sociosSQL.append(f"{i} varchar(200),")
sociosSQL.append("faixaEtaria varchar(200)")

simples = ["cnpjBasico","opcaoSimples","dataOpcao","dataExclusao","opcaoMei","dataOpcaoMei","dataExclusaoMei"]
simplesSQL = ["cnpjBasico nvarchar(200) primary key,"]

for i in simples[1:-1]:
    simplesSQL.append(f"{i} varchar(200),")
simplesSQL.append("dataExclusaoMei varchar(200)")


    
with open("config") as f:
    lines= f.readlines()
    user = lines[0]
    password = lines[1]

conn = mysql.connector.connect(host='localhost',
                                         database='public',
                                         user=user,
                                         password=password)
print("feita conecao")

cursor = conn.cursor()

try:
    cursor.execute('''CREATE DATABASE public;''')
except Exception as e: print(e)
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
        encoding='latin-1',)
    for row in df.itertuples():
        try:
            a= f"""INSERT INTO public.{chave.lower()} (codigo, descricao) VALUES ("{row.codigo}","{row.descricao}")"""
            cursor.execute(a)
        except:
            pass

print("terminado atributos")
for chave,valor in {'EMPRESAS':["EMPRESASALL",empresasSQL,empresas],'ESTABELECIMENTOS':["ESTABELECIMENTOSALL",estabelecimentoSQL,estabelecimento],'SOCIOS':["SOCIOSALL",sociosSQL,socios],"SIMPLES":["SIMPLESALL",simplesSQL,simples]}.items():
    if chave == 'EMPRESAS':
        cursor.execute('USE public')
        conn.commit()
        cursor.execute(f"DROP TABLE IF EXISTS {chave}")
        conn.commit()
        cursor.execute(f'''
        	    CREATE TABLE {chave} (
                {''.join(empresasSQL)}
        		);
                   ''')
        conn.commit()
        
        df = pd.read_csv("/".join(__file__.split("\\")[:-1])+ f"/{valor[0]}",sep=';',names =valor[2], 
            encoding='latin-1')
        for row in df.itertuples() :
                por=['NÃO INFORMADO','MICRO EMPRESA','EMPRESA DE PEQUENO PORTE','DEMAIS']
                
                if row.porte== 0:
                    c=por[0]
                if row.porte == 1:
                    c=por[1]
                if row.porte == 3:
                    c=por[2]
                if row.porte == 5:
                    c=por[3]
                if row.cnpjBasico:
                    cnpj = str(row.cnpjBasico)
                    cnpj = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:]}/"
                    
                a= f"""INSERT INTO public.{chave.lower()} ({",".join(valor[2])}) VALUES
                ("{cnpj}","{row.nomeSocial}","{row.naturezaJuridico}","{row.qualificacaoCodigo}","{row.capital}","{c}","{row.responsavel}");"""
                
                cursor.execute(a)
                conn.commit()
        print("terminado empresas")
    if chave == 'SOCIOS':
        cursor.execute('USE public')
        conn.commit()
        cursor.execute(f"DROP TABLE IF EXISTS {chave} ")
        conn.commit()
        cursor.execute(f'''
        	    CREATE TABLE {chave} (
                {''.join(valor[1])}
        		)
                
                   ''')
        conn.commit()
        df = pd.read_csv("/".join(__file__.split("\\")[:-1])+ f"/{valor[0]}",sep=';',names =valor[2], 
            encoding='latin-1', error_bad_lines=False)
        for row in df.itertuples() :
            if row.identificadorSocio:
                
                identificadorSocio = ["PESSOA JURÍDICA", "PESSOA FÍSICA"," ESTRANGEIRO"][int(row.identificadorSocio)-1]
            if row.dataEntradaSociedade:
                data = str(row.dataEntradaSociedade)
 
                dataEntradaSociedade = f'{data[:4]}-{data[4:6]}-{"0"*(2-len(data[7:]))}{data[7:]}'
            if row.cnpjBasico:
                cnpj = str(row.cnpjBasico)
                cnpj = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:]}/"
                
           
            a= f"""INSERT INTO public.{chave.lower()} ({",".join(valor[2])}) VALUES 
            ("{cnpj}",
            "{identificadorSocio}",
            "{row.nomeSociorazaoSocial}",
            "{row.cnpjcpfSocio}","{row.qualificacaoCodigoSocio}",
            "{dataEntradaSociedade}","{row.paisSocio}","{row.represetante}","{row.nomeRepresentante}","{row.qualificacoesRepresentante}","{row.faixaEtaria}")"""
            
            cursor.execute(a)
            conn.commit()
            
        print("terminado socios")

    if chave == 'ESTABELECIMENTOS':
        cursor.execute('USE public')
        conn.commit()
        cursor.execute(f"DROP TABLE IF EXISTS {chave}")
        conn.commit()
        
        cursor.execute(f'''
         	    CREATE TABLE {chave} (
                {''.join(valor[1])}
         		);
                   ''')
        conn.commit()
        df = pd.read_csv("/".join(__file__.split("\\")[:-1])+ f"/{valor[0]}",sep=';',names =valor[2], 
            encoding='latin-1', error_bad_lines=False)
        for row in df.itertuples():
            try:
                situ = ['NULA', 'ATIVA', 'SUSPENSA', 'INAPTA', 'BAIXADA']
                if int(row.situacaoCadastral) <5:
                    a = situ[int(row.situacaoCadastral)-1]
                else:a = situ[-1]
            except Exception as e: print(e) 
      
            try:   
                ma=['MATRIX','FILIAL']
                mamama=ma[int(row.matriz)-1]
            except Exception as e: print(e)
            data=str(row.dataAtividade)
            ano =data[:4]
            mes =data[4:6]
            dia= data[7:]
            inicio = f'{ano}-{mes}-{"0"*(2-len(dia))}{dia}'
            
            dataEspecial= row.dataSituacaoEspecial
            
            if len(str(row.dataSituacaoEspecial)) >4:
                data=str(row.dataSituacaoEspecial)
                ano =data[:4]
                mes =data[4:6]
                dia= data[7:]
                dataEspecial = f'{ano}-{mes}-{"0"*(2-len(dia))}{dia}'
                
            dataCadastral=row.dataSituacaoCadastral
            if len(str(dataCadastral)) >4:
                data=str(row.dataSituacaoCadastral)
                ano =data[:4]
                mes =data[4:6]
                dia= data[7:]
                dataEspecial = f'{ano}-{mes}-{"0"*(2-len(dia))}{dia}'
            if row.cnpjBasico:
                cnpj = str(row.cnpjBasico)
                cnpj = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:]}/"
            if row.cnpjDv:
                cnpjDv = str(row.cnpjDv)
                cnpjDv = f"-{cnpjDv}"
            
            cnpjOrden = str(row.cnpjOrdem)  
            
            while len(cnpjOrden) < 4:
                cnpjOrden = f"0{cnpjOrden}"
            
            a= f"""INSERT INTO public.{chave.lower()} ({",".join(valor[2])}) VALUES 
            (
            "{cnpj}",
           "{cnpjOrden}",
           "{cnpjDv}",
           "{mamama}",
           "{row.nomeFantasia}",
           "{a}","{row.dataSituacaoCadastral}",
           "{row.motivoSituacaoCadastral}","{row.nomeCidadeExterior}","{row.pais}","{inicio}",
           "{row.cnaePrincipal}","{row.cnaeSecundario}","{row.tipoLogradouro}","{row.logradouro}",
           "{row.numero}",
           "{row.complemento}",
           "{row.bairro}","{row.cep}","{row.uf}","{row.municipio}","{row.ddd1}","{row.telefone1}","{row.ddd2}","{row.telefone2}","{row.dddFax}","
           {row.fax}","{row.correioEletronico}","{row.situacaoEspecial}","{dataEspecial}")"""

            cursor.execute(a)
            conn.commit()
            print("terminado estabelecimentos")
    if chave == "SIMPLES":
        
        cursor.execute('USE public')
        conn.commit()
        cursor.execute(f"DROP TABLE IF EXISTS {chave.lower()};")
        conn.commit()
        
        cursor.execute(f'''
         	    CREATE TABLE {chave} (
                {''.join(valor[1])}
         		);
                   ''')
        conn.commit()
        df = pd.read_csv("/".join(__file__.split("\\")[:-1])+ f"/{valor[0]}",sep=';',names =valor[2], 
            encoding='latin-1', error_bad_lines=False)
        
        for row in df.itertuples() :
            dataOp= row.dataOpcao
            
            if len(str(row.dataOpcao)) >4:
                data=str(row.dataOpcao)
                ano =data[:4]
                mes =data[4:6]
                dia= data[7:]
                dataOp = f'{ano}-{mes}-{"0"*(2-len(dia))}{dia}'
            dataEx= row.dataExclusao
            
            if len(str(row.dataExclusao)) >4:
                data=str(row.dataExclusao)
                ano =data[:4]
                mes =data[4:6]
                dia= data[7:]
                dataEx = f'{ano}-{mes}-{"0"*(2-len(dia))}{dia}'
                
            dataExMEI= row.dataExclusaoMei

            if len(str(row.dataExclusaoMei)) >4:
                data=str(row.dataExclusaoMei)
                ano =data[:4]
                mes =data[4:6]
                dia= data[7:]
                dataExMEI = f'{ano}-{mes}-{"0"*(2-len(dia))}{dia}'
            dafaopmei= row.dataOpcaoMei

            if len(str(row.dataOpcaoMei)) >4:
                data=str(row.dataOpcaoMei)
                ano =data[:4]
                mes =data[4:6]
                dia= data[7:]
                dafaopmei = f'{ano}-{mes}-{"0"*(2-len(dia))}{dia}'
            if row.cnpjBasico:
                cnpj = row.cnpjBasico
                cnpj = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:]}"
            a= f"""INSERT INTO public.{chave.lower()} ({",".join(valor[2])}) VALUES 
            (
            "{cnpj}",
            "{row.opcaoSimples}",
            "{dataOp}",
            "{dataEx}",
            "{row.opcaoMei}",
            "{dafaopmei}","{dataExMEI}")"""
            cursor.execute(a)
            conn.commit()
   
        print("terminado simples")


conn.close()
cursor.close()
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