import time
from turtle import onclick

import mysql.connector
import pandas as pd
import PySimpleGUI as sg


def app():
    with open("config") as f:
        lines= f.readlines()
        lines = [x[:-1] for x in lines]

       
        

    conn = mysql.connector.connect(host="localhost",
                                         database="public",
                                         user="root",
                                         password="225236")
    print("feita conecao")
    cursor = conn.cursor()
    sg.theme('Dark Grey 13')
    
    # INPUTS:
    # rs - Razao Social          # CEP -CEP                               # cnpj - CNPJ Basico -- adicionar
    # CNAE - Atvidade Principal  # DDD - DDD                              # ql - Qualificaçao do responsável --adicionar
    # NJ - Natural Juridica      # datade - Data de abertura  a partir    # efr - Ente federativo responsavel -- adicionar
    # UF - Estado                # dataate - Data de abertura ate
    # mn - Municipio             # apartir - Capital Social a partir
    # bairro - bairro            # ate - Capital social ate

    layout = [
        [sg.Text("Razão social ou nome fantasia:"), sg.Input(key="estabelecimentos.nomeFantasia"), sg.Text("Atividade Principal (CNAE):"), sg.Input(key="cnae_principal.descricao")],
        [sg.Text("Natureza Jurídica: "), sg.Input(key="naturezajuridico.descricao"), sg.Text("Atividade secundaria (CNAE segundario):"), sg.Input(key="cnae_secundario.descricao")],
        [sg.Text("Situação cadastral: "), sg.Combo(['NULA', 'ATIVA', 'SUSPENSA', 'INAPTA', 'BAIXADA'],key="estabelecimentos.situacaoCadastral")],
        [sg.Text("Estado (UF)"), sg.Input(key="estabelecimentos.uf", size=(3, 1)), sg.Text("Municipio"), sg.Input(key="estabelecimento_municipio.descricao")],
        [sg.Text("Bairro"), sg.Input(key="estabelecimentos.bairro"),sg.Text("Rua"), sg.Input(key="estabelecimentos.logradouro"),sg.Text("CEP"), sg.Input(key="estabelecimentos.cep", size=(15, 1)), sg.Text("DDD - 2 digitos"), sg.Input(key="estabelecimentos.ddd1", size=(2,1))],
        [sg.Text("Data de abertura - A partir de"), sg.Input(key="ab"), sg.Text("Data de abertura - Até"), sg.Input(key="abt")],
        [sg.Text("Capital Social - A partir de"), sg.Input(key="emCDE"), sg.Text("Capital Social - Ate"), sg.Input(key="emCATE")],
        [sg.Checkbox("Somente mei", key="simples.opcaoMei 3"), sg.Checkbox("Excluir MEI", key="simples.opcaoMei 4"), sg.Checkbox("Somente Matriz", key="estabelecimentos.matriz 0")],
        [sg.Checkbox("Somente filial", key="estabelecimentos.matriz 2"), sg.Checkbox("Com contato de telefone", key="estabelecimentos.telefone1"), sg.Checkbox("Somente fixo", key="sf"), sg.Checkbox("Somente celular", key="sc")],
        [sg.Text("Nome do arquivo para qual sera exportado ",), sg.Input(key="nome_arquivo",size=(10,1)),sg.Button('Exportar para xml "pesquisa.xml"', size=(20, 2)),sg.Button('Exportar para csv "pesquisa.csv"', size=(20, 2)), ],
        [sg.Text("", key="response")]]

        # CHECKBOX:
        # sm - Somente MEI      # sfl - somente filial          # ias - Incluir atividades secundarias
        # em - Excluir MEI      # st - com contato de telefone
        # sma - Somente Matriz  # sc - Somente Celular
        # sf - Somente Fixo     # ce - Com e-mail

    window = sg.Window('CNPJ - PESQUISA', layout=layout)
    while True:
        nome_arquivo = 'pesquisa'
        evento, valores = window.read()

        if evento == sg.WIN_CLOSED:
            break
        elif evento == 'Exportar para xml "pesquisa.xml"':
            layout1 = [[sg.Text("Aguarde, Carregando....")],[sg.Text("O janela se feixara depois de finalizado a buscas")]]
            sg.Window("Carregando....", layout=layout1, finalize=True)

            
            
            # pegando todos os dados:
            example = """
           select CONCAT( empresas.cnpjBasico,
			public.estabelecimentos.cnpjOrdem
            ,public.estabelecimentos.cnpjDv ) as cnpj,
            public.empresas.nomeSocial
            ,public.naturezajuridico.descricao natureza_juridico_Empresa
            ,qualificacao_Empresa.descricao empresa_qualificacao
            ,empresas.capital
            ,empresas.porte,
             public.empresas.responsavel,
            public.estabelecimentos.matriz,
             public.estabelecimentos.nomeFantasia, 
             public.estabelecimentos.situacaoCadastral
             ,public.estabelecimentos.dataSituacaoCadastral
             , public.estabelecimentos.nomeCidadeExterior
             , estabelecimento_pais.descricao estabelecimento_Pais
             , public.estabelecimentos.dataAtividade
             , cnae_principal.descricao cnae_principal
             , cnae_secundario.descricao cnaeSecundario
             , public.estabelecimentos.tipoLogradouro
             , public.estabelecimentos.logradouro
             , public.estabelecimentos.numero
             ,public.estabelecimentos.complemento
             ,public.estabelecimentos.bairro
             ,public.estabelecimentos.cep
             , public.estabelecimentos.uf
             ,estabelecimento_municipio.descricao estabelecimento_municipio
             , public.estabelecimentos.ddd1
             ,public.estabelecimentos.telefone1
             , public.estabelecimentos.dddFax 
             , public.estabelecimentos.fax
             , public.estabelecimentos.correioEletronico
             , public.estabelecimentos.situacaoEspecial,public.estabelecimentos.dataSituacaoEspecial,
             socios.identificadorSocio,
             public.socios.nomeSociorazaoSocial,
             public.socios.cnpjcpfSocio,
             public.socios.dataEntradaSociedade,
             socios.paisSocio
             ,qualificacao_repre.descricao qualificacao_repre,
             public.socios.nomeRepresentante,
             qualificacao_socio.descricao qualificacao_socio
             ,public.socios.faixaEtaria 
             from empresas 
             left outer join simples on empresas.cnpjBasico = simples.cnpjBasico
             left outer join socios on socios.cnpjBasico = empresas.cnpjBasico
             inner join estabelecimentos on empresas.cnpjBasico = estabelecimentos.cnpjBasico
             left outer join pais estabelecimento_pais on estabelecimentos.pais =estabelecimento_pais.codigo
             left outer join municipio estabelecimento_municipio on estabelecimentos.municipio= estabelecimento_municipio.codigo
             left outer join naturezajuridico on empresas.naturezaJuridico=naturezajuridico.codigo
             left outer join qualificacao qualificacao_Empresa on empresas.qualificacaoCodigo=qualificacao_Empresa.codigo 
             left outer join qualificacao qualificacao_socio on socios.qualificacaoCodigoSocio = qualificacao_socio.codigo
             left outer join qualificacao qualificacao_repre on socios.qualificacoesRepresentante = qualificacao_repre.codigo
             left outer join cnae  cnae_principal on estabelecimentos.cnaePrincipal  = cnae_principal.codigo
             left outer join cnae  cnae_secundario on estabelecimentos.cnaeSecundario  = cnae_secundario.codigo
             left outer join pais socios_Pais on socios.paisSocio = socios_Pais.codigo
             """
            num = 1
            aber= []
            capitald = []
            
            for chave,valor in valores.items():
       
                if chave == 'nome_arquivo':
                    if valor:
                        nome_arquivo = valor
                    continue
                
                if num:
                  
                    if valor:
     
                        if chave =="emCDE":
                            capitald.append(valor)
                            continue
                        if chave == "emCATE":
                            capitald.append(valor)
                       
                        if len(capitald) ==2:
                            example+= f'where empresas.capital >= {capitald[0]} and empresas.capital <= {capitald[1]} '
                            continue
                        if chave == 'ab':
                            aber.append(valor)
                            continue
                        if chave =='abt':
                            num-=1
                            aber.append(valor)
                                          
                        if chave =='sf':
                            num-=1
                            example += 'where estabelecimentos.telefone1 not like "9%" or  estabelecimentos.telefone1 not like "8%"  '
                            continue
                        if chave == 'sc':
                            num-=1
                            example += 'where estabelecimentos.telefone1  like "9%" or  estabelecimentos.telefone1  like "8%"  '
                            continue
     
                        if chave =='estabelecimentos.telefone1':
                            num-=1
                            valor='nan'
                           
                            example+= f'where {chave} like "%{valor}%"'
                            continue
                        if chave[-1] == "0": 
                            chave = chave[:-2]
                            valor = "MATRIX"
                        if chave[-1] == "2": 
                            chave = chave[:-2]
                            valor = "FILIAL"
                        if chave[-1] == "3":
                            chave = chave[:-2]
                            valor = "S"
                        if chave[-1] == "4":
                            chave = chave[:-2]
                            valor = "N"
                        num-=1
                        if len(aber) ==2:
                            for n,i in enumerate(aber):
                             
                                dia = aber[n][:2]
                                mes= aber[n][3:5]
                                ano = aber[n][6:11]
                                aber[n] = f'{ano}-{mes}-{dia}'
                                 
                            example+= f'where estabelecimentos.dataAtividade >= "{aber[0]}" and estabelecimentos.dataAtividade <= "{aber[1]}" '
                            continue
                        example+= f'where {chave} like "%{valor}%"'
      
                else:
                    if valor:
                        if chave =="emCDE":
                            capitald.append(valor)
                            continue
                        if chave == "emCATE":
                            capitald.append(valor)
                        if len(capitald) ==2:
                            example+= f'end empresas.capital >= {capitald[0]} and empresas.capital <= {capitald[1]} '
                            continue
                        if chave == 'ab':
                            aber.append(valor)
                            continue
                        if chave =='abt':
                            num-=1
                            aber.append(valor)
                      
                        if chave =='sf':
                            num-=1
                            example += ' and estabelecimentos.telefone1 not like "9%" or  estabelecimentos.telefone1 not like "8%"'
                            continue
                        if chave == 'sc':
                            num-=1
                            example += ' and estabelecimentos.telefone1  like "9%" or  estabelecimentos.telefone1  like "8%"'
                            continue
                        
                        if chave[-1] == "0": 
                            chave = chave[:-2]
                            valor = "MATRIX"
                        if chave[-1] == "2": 
                            chave = chave[:-2]
                            valor = "FILIAL"
                        if chave[-1] == "3":
                            chave = chave[:-2]
                            valor = "S"
                        if chave[-1] == "4":
                            chave = chave[:-2]
                            valor = "N"
                        if len(aber) ==2:
                            for n,i in enumerate(aber):
                             
                                dia = aber[n][:2]
                                mes= aber[n][3:5]
                                ano = aber[n][6:11]
                                aber[n] = f'{ano}-{mes}-{dia}'
                                 
                            example+= f'and estabelecimentos.dataAtividade >= {aber[0]} and estabelecimentos.dataAtividade <= {aber[1]} '
                            continue
                        
                        if valor == True:example+= f' and {chave} like "%{chave}%"'
                        else:example+= f' and {chave} like "%{valor}%"'

            cursor.execute(example)
            
            
            a= cursor.fetchall()
            if a:
                colunas =["CNPJ","Razão_Social","Natureza_Jurídica","Qualificação","Capital","Porte","Responsável","Matriz_ou_Filial","Nome_de_Fantasia","Situação_Cadastral","Data_da_Situação_Cadastral","Nome_da_Cidade_no_Exterior","País","Data_Início_Atividades","CNAE_Principal","CNAE_Secundários","Tipo_de_Logradouro","Logradouro","Numero","Complemento","Bairro","CEP","UF","Município" ,"DDD1","Telefone_1","DDD_Fax","FAX","E-Mail","Situação_Especial","Data_Situação_Especial","identificadorSocio","Nome_dos_Sócios","CPF_ou_CNPJ_Sócios","Data_Entrada_na_Sociedade","Pais_Socio","Qualificação_Representante","Nome_do_Representante","qualificacao_socio","faixaEtaria"]     
                frame= pd.DataFrame(a,columns=colunas)
                frame.to_xml(nome_arquivo+'.xml')
            sg.Popup(f"Foram encontrados {len(a)} resultados para a sua busca", keep_on_top=True )
                
           
        elif evento == 'Exportar para csv "pesquisa.csv"':
            layout1 = [[sg.Text("Aguarde, Carregando....")],[sg.Text("O janela se feixara depois de finalizado a buscas")]]
            sg.Window("Telegram bot", layout=layout1, finalize=True)
            # pegando todos os dados:
            example = """
           select CONCAT( empresas.cnpjBasico,
			public.estabelecimentos.cnpjOrdem
            ,public.estabelecimentos.cnpjDv ) as cnpj,
            public.empresas.nomeSocial
            ,public.naturezajuridico.descricao natureza_juridico_Empresa
            ,qualificacao_Empresa.descricao empresa_qualificacao
            ,empresas.capital
            ,empresas.porte,
             public.empresas.responsavel,
            public.estabelecimentos.matriz,
             public.estabelecimentos.nomeFantasia, 
             public.estabelecimentos.situacaoCadastral
             ,public.estabelecimentos.dataSituacaoCadastral
             , public.estabelecimentos.nomeCidadeExterior
             , estabelecimento_pais.descricao estabelecimento_Pais
             , public.estabelecimentos.dataAtividade
             , cnae_principal.descricao cnae_principal
             , cnae_secundario.descricao cnaeSecundario
             , public.estabelecimentos.tipoLogradouro
             , public.estabelecimentos.logradouro
             , public.estabelecimentos.numero
             ,public.estabelecimentos.complemento
             ,public.estabelecimentos.bairro
             ,public.estabelecimentos.cep
             , public.estabelecimentos.uf
             ,estabelecimento_municipio.descricao estabelecimento_municipio
             , public.estabelecimentos.ddd1
             ,public.estabelecimentos.telefone1
             , public.estabelecimentos.dddFax 
             , public.estabelecimentos.fax
             , public.estabelecimentos.correioEletronico
             , public.estabelecimentos.situacaoEspecial,public.estabelecimentos.dataSituacaoEspecial,
             socios.identificadorSocio,
             public.socios.nomeSociorazaoSocial,
             public.socios.cnpjcpfSocio,
             public.socios.dataEntradaSociedade,
             socios.paisSocio
             ,qualificacao_repre.descricao qualificacao_repre,
             public.socios.nomeRepresentante,
             qualificacao_socio.descricao qualificacao_socio
             ,public.socios.faixaEtaria 
             from empresas 
             left outer join simples on empresas.cnpjBasico = simples.cnpjBasico
             left outer join socios on socios.cnpjBasico = empresas.cnpjBasico
             inner join estabelecimentos on empresas.cnpjBasico = estabelecimentos.cnpjBasico
             left outer join pais estabelecimento_pais on estabelecimentos.pais =estabelecimento_pais.codigo
             left outer join municipio estabelecimento_municipio on estabelecimentos.municipio= estabelecimento_municipio.codigo
             left outer join naturezajuridico on empresas.naturezaJuridico=naturezajuridico.codigo
             left outer join qualificacao qualificacao_Empresa on empresas.qualificacaoCodigo=qualificacao_Empresa.codigo 
             left outer join qualificacao qualificacao_socio on socios.qualificacaoCodigoSocio = qualificacao_socio.codigo
             left outer join qualificacao qualificacao_repre on socios.qualificacoesRepresentante = qualificacao_repre.codigo
             left outer join cnae  cnae_principal on estabelecimentos.cnaePrincipal  = cnae_principal.codigo
             left outer join cnae  cnae_secundario on estabelecimentos.cnaeSecundario  = cnae_secundario.codigo
             left outer join pais socios_Pais on socios.paisSocio = socios_Pais.codigo
             """
            num = 1
            capitald = []
            aber= []
            for chave,valor in valores.items():
                if chave == 'nome_arquivo':
                    if valor:
                        nome_arquivo = valor
                    continue
                if num:
                    if valor:
                        if chave =="emCDE":
                            capitald.append(valor)
                            continue
                        if chave == "emCATE":
                            capitald.append(valor)
                        if len(capitald) ==2:
                            example+= f'where empresas.capital >= {capitald[0]} and empresas.capital <= {capitald[1]} '
                            continue
                        if chave =='sf':
                            num-=1
                            example += ' where estabelecimentos.telefone1 not like "9%" or  estabelecimentos.telefone1 not like "8%"  '
                            continue
                        if chave == 'ab':
                            aber.append(valor)
                            continue
                        if chave =='abt':
                            num-=1
                            aber.append(valor)
                    
                        if chave == 'sc':
                            num-=1
                            example += ' where estabelecimentos.telefone1  like "9%" or  estabelecimentos.telefone1  like "8%"  '
                            continue
                        if chave =='estabelecimentos.telefone1':
                            num-=1
                            valor='nan'
                           
                            example+= f'where {chave} like "%{valor}%"'
                            continue
                        if chave[-1] == "0": 
                            chave = chave[:-2]
                            valor = "MATRIX"
                        if chave[-1] == "2": 
                            chave = chave[:-2]
                            valor = "FILIAL"
                        if chave[-1] == "3":
                            chave = chave[:-2]
                            valor = "S"
                        if chave[-1] == "4":
                            chave = chave[:-2]
                            valor = "N"
                        if len(aber) ==2:
                            for n,i in enumerate(aber):
                             
                                dia = aber[n][:2]
                                mes= aber[n][3:5]
                                ano = aber[n][6:11]
                                aber[n] = f'{ano}-{mes}-{dia}'
                                 
                            example+= f'where estabelecimentos.dataAtividade >= {aber[0]} and estabelecimentos.dataAtividade <= {aber[1]}'
                            continue
                        num-=1
                        example+= f'where {chave} like "%{valor}%"'
                else:
                    if valor:
                        if chave =="emCDE":
                            capitald.append(valor)
                            continue
                        if chave == "emCATE":
                            capitald.append(valor)
                        if len(capitald) ==2:
                            example+= f'and empresas.capital >= {capitald[0]} and empresas.capital <= {capitald[1]} '
                            continue
                        if chave =='sf':
                            num-=1
                            example += ' and estabelecimentos.telefone1 not like "9%" or  estabelecimentos.telefone1 not like "8%"  '
                            continue
                        if chave == 'sc':
                            num-=1
                            example += ' and estabelecimentos.telefone1  like "9%" or  estabelecimentos.telefone1  like "8%"  '
                            continue
                        if chave == 'ab':
                            aber.append(valor)
                            continue
                        if chave =='abt':
                            num-=1
                            aber.append(valor)
                       
                        if chave[-1] == "0": 
                            chave = chave[:-2]
                            valor = "MATRIX"
                        if chave[-1] == "2": 
                            chave = chave[:-2]
                            valor = "FILIAL"
                        if chave[-1] == "3":
                            chave = chave[:-2]
                            valor = "S"
                        if chave[-1] == "4":
                            chave = chave[:-2]
                            valor = "N"
                        if len(aber) ==2:
                            for n,i in enumerate(aber):
                             
                                dia = aber[n][:2]
                                mes= aber[n][3:5]
                                ano = aber[n][6:11]
                                aber[n] = f'{ano}-{mes}-{dia}'
                                 
                            example+= f'and estabelecimentos.dataAtividade >= {aber[0]} and estabelecimentos.dataAtividade <= {aber[1]} '
                            continue
                        if valor == True:example+= f' and {chave} like "%{chave}%"'
                        else:example+= f' and {chave} like "%{valor}%"'

            cursor.execute(example)
            a= cursor.fetchall()
            if a:
                colunas= ["CNPJ","Razão_Social","Natureza_Jurídica","Qualificação","Capital","Porte","Responsável","Matriz_ou_Filial","Nome_de_Fantasia","Situação_Cadastral","Data_da_Situação_Cadastral","Nome_da_Cidade_no_Exterior","País","Data_Início_Atividades","CNAE_Principal","CNAE_Secundários","Tipo_de_Logradouro","Logradouro","Numero","Complemento","Bairro","CEP","UF","Município" ,"DDD1","Telefone_1","DDD_Fax","FAX","E-Mail","Situação_Especial","Data_Situação_Especial","identificadorSocio","Nome_dos_Sócios","CPF/CNPJ_Sócios","Data_Entrada_na_Sociedade","Pais_Socio","Qualificação_Representante","Nome_do_Representante","qualificacao_socio","faixaEtaria"]     
                frame= pd.DataFrame(a,columns=colunas)
                frame.to_csv(nome_arquivo+'.csv')
            sg.Popup(f"Foram encontrados {len(a)} resultados para a sua busca", keep_on_top=True )
            


    
        
            
            
            
               
                                
app()
