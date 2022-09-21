import shutil
from os import walk
import sys

""" 
Arquivo python para leer todos os arquivos em uma pasta e juntar todos em 1 arquivo

como usar:
    python joinFiles.py NomeDaPasta LocalDoNovoArquivo+NomeArquivo
exemplo:
    python joinFiles.py EMPRESAS todasEmpresas
    
ira buscar os arquivos na pasta ./files/EMPRESAS/ e criara o arquivo em ./files/todasEmpresas
    
A pasta com os arquivos tem que estar dentro de ./files/
E o arquivo criado estara dentro de ./files/

"""
def joinfiles(BasePath,filename):
    with open(filename,'wb') as wfd:
        for f in next(walk(BasePath), (None, None, []))[2]:
            with open(BasePath + f,'rb') as fd:
                shutil.copyfileobj(fd, wfd)

""" Em caso que queira modificar a localizacao da pasta ou onde arquivo é salvo so mudar a linha abaixo """
joinfiles(f"./files/{sys.argv[1]}/",f"./files/{sys.argv[2]}")