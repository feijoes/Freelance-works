
import PySimpleGUI as sg
import pandas as pd
import mysql.connector
def app():
    conn = mysql.connector.connect(host='localhost',
                                         database='public',
                                         user='root',
                                         password='225236')
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
        [sg.Text("Natureza Jurídica: "), sg.Input(key="naturezajuridico.descricao"), sg.Text("Atividade secundaria (CNAE segundario):"), sg.Input(key="'cnae_secundario'.descricao")],
        [sg.Text("Situação cadastral: "), sg.Combo(['NULA', 'ATIVA', 'SUSPENSA', 'INAPTA', 'BAIXADA'],key="estabelecimentos.situacaoCadastral")],
        [sg.Text("Estado (UF)"), sg.Input(key="estabelecimentos.uf", size=(3, 1)), sg.Text("Municipio"), sg.Input(key="estabelecimento_municipio.descricao")],
        [sg.Text("Bairro"), sg.Input(key="estabelecimentos.bairro"),sg.Text("Rua"), sg.Input(key="estabelecimentos.logradouro"), sg.Text("Numero"), sg.Input(key="estabelecimentos.numero", size=(12,1)),sg.Text("CEP"), sg.Input(key="estabelecimentos.cep", size=(15, 1)), sg.Text("DDD - 2 digitos"), sg.Input(key="estabelecimentos.ddd1", size=(2,1))],
        [sg.Text("Data de abertura - A partir de"), sg.Input(key="socio.dataOpcao"), sg.Text("Data de abertura - Até"), sg.Input(key="simples.dataOpcao")],
        [sg.Text("Capital Social - A partir de"), sg.Input(key="empresas.capital"), sg.Text("Capital Social - Ate"), sg.Input(key="empresas.capital")],
        [sg.Checkbox("Somente mei", key="simples.opcaoMei 3"), sg.Checkbox("Excluir MEI", key="simples.opcaoMei 4"), sg.Checkbox("Somente Matriz", key="estabelecimentos.matriz 0"), sg.Checkbox("Somente fixo", key="sf")],
        [sg.Checkbox("Somente filial", key="estabelecimentos.matriz 1"), sg.Checkbox("Com contato de telefone", key="estabelecimentos.telefone1"), sg.Checkbox("Somente celular", key="sc")],
        [sg.Button('Exportar para xml "pesquisa.xml"', size=(20, 2)),sg.Button('Exportar para csv "pesquisa.csv"', size=(20, 2))],
        [sg.Text("", key="response")]]

        # CHECKBOX:
        # sm - Somente MEI      # sfl - somente filial          # ias - Incluir atividades secundarias
        # em - Excluir MEI      # st - com contato de telefone
        # sma - Somente Matriz  # sc - Somente Celular
        # sf - Somente Fixo     # ce - Com e-mail

    window = sg.Window('CNPJ - PESQUISA', layout=layout)
    while True:
        evento, valores = window.read()
        if evento == sg.WIN_CLOSED:
            break
        elif evento == 'Exportar para xml "pesquisa.xml"':
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
             public.socios.dataSituacaoCadastral,
             public.socios.nomeCidadeExterior
             ,socios.paisSocio
             ,qualificacao_repre.descricao qualificacao_repre,
             public.socios.nomeRepresentante,
             qualificacao_socio.descricao qualificacao_socio
             ,public.socios.faixaEtaria 
             from empresas 
             left outer join simples on empresas.cnpjBasico = simples.cnpjBasico
             inner join socios on socios.cnpjBasico = empresas.cnpjBasico
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
            for chave,valor in valores.items():
                
                if num:
                    if valor:
                        if chave =='estabelecimentos.telefone1':
                            num-=1
                            valor='nan'
                            print(chave)
                            example+= f'where {chave} like "%{valor}%"'
                            continue
                        if chave[-1] == "0": 
                            chave = chave[:-2]
                            valor = "MATRIX"
                        if chave[-1] == "1": 
                            chave = chave[:-2]
                            valor = "FILIAL"
                        if chave[-1] == "3":
                            chave = chave[:-2]
                            valor = "S"
                        if chave[-1] == "4":
                            chave = chave[:-2]
                            valor = "N"
                        num-=1
                        example+= f'where {chave} like "%{valor}%"'
                else:
                    if valor:
                        print(chave,valor)
                        if chave[-1] == "0": 
                            chave = chave[:-2]
                            valor = "MATRIX"
                        if chave[-1] == "1": 
                            chave = chave[:-2]
                            valor = "FILIAL"
                        if chave[-1] == "3":
                            chave = chave[:-2]
                            valor = "S"
                        if chave[-1] == "4":
                            chave = chave[:-2]
                            valor = "N"
                        print(chave,valor)
                        if valor == True:example+= f' and {chave} like "%{chave}%"'
                        else:example+= f' and {chave} like "%{valor}%"'
            print(example)
            cursor.execute(example)
            a= cursor.fetchall()
            
            colunas =["Cnpj","nomeSocial","natureza_juridico_Empresa","empresa_qualificacao","capital","porte","responsavel","matriz","nomeFantasia","situacaoCadastral","dataSituacaoCadastral","nomeCidadeExterior","estabelecimento_Pais","dataAtividade","cnae_principal","cnae_secundario","tipoLogradouro","logradouro","numero","complemento","bairro","cep","uf","estabelecimento_municipio","ddd1","telefone1","dddFax" ,"fax","correioEletronico","situacaoEspecial","dataSituacaoEspecial","identificadorSocio","nomeSociorazaoSocial","cnpjcpfSocio","dataEntradaSociedade","dataSituacaoCadastral","nomeCidadeExterior","paisSocio","qualificacao_repre","nomeRepresentante","qualificacao_socio","faixaEtaria"]     
            frame= pd.DataFrame(a,columns=colunas)
            print(frame)
            frame.to_xml("pesquisa.xml")
        elif evento == 'Exportar para csv "pesquisa.csv"':
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
             public.socios.dataSituacaoCadastral,
             public.socios.nomeCidadeExterior
             ,socios.paisSocio
             ,qualificacao_repre.descricao qualificacao_repre,
             public.socios.nomeRepresentante,
             qualificacao_socio.descricao qualificacao_socio
             ,public.socios.faixaEtaria 
             from empresas 
             left outer join simples on empresas.cnpjBasico = simples.cnpjBasico
             inner join socios on socios.cnpjBasico = empresas.cnpjBasico
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
            for chave,valor in valores.items():
                
                if num:
                    if valor:
                        if chave =='estabelecimentos.telefone1':
                            num-=1
                            valor='nan'
                            print(chave)
                            example+= f'where {chave} like "%{valor}%"'
                            continue
                        if chave[-1] == "0": 
                            chave = chave[:-2]
                            valor = "MATRIX"
                        if chave[-1] == "1": 
                            chave = chave[:-2]
                            valor = "FILIAL"
                        if chave[-1] == "3":
                            chave = chave[:-2]
                            valor = "S"
                        if chave[-1] == "4":
                            chave = chave[:-2]
                            valor = "N"
                        num-=1
                        example+= f'where {chave} like "%{valor}%"'
                else:
                    if valor:
                        print(chave,valor)
                        if chave[-1] == "0": 
                            chave = chave[:-2]
                            valor = "MATRIX"
                        if chave[-1] == "1": 
                            chave = chave[:-2]
                            valor = "FILIAL"
                        if chave[-1] == "3":
                            chave = chave[:-2]
                            valor = "S"
                        if chave[-1] == "4":
                            chave = chave[:-2]
                            valor = "N"
                        print(chave,valor)
                        if valor == True:example+= f' and {chave} like "%{chave}%"'
                        else:example+= f' and {chave} like "%{valor}%"'
            print(example)
            cursor.execute(example)
            a= cursor.fetchall()
            
            colunas =["Cnpj","nomeSocial","natureza_juridico_Empresa","empresa_qualificacao","capital","porte","responsavel","matriz","nomeFantasia","situacaoCadastral","dataSituacaoCadastral","nomeCidadeExterior","estabelecimento_Pais","dataAtividade","cnae_principal","cnae_secundario","tipoLogradouro","logradouro","numero","complemento","bairro","cep","uf","estabelecimento_municipio","ddd1","telefone1","dddFax" ,"fax","correioEletronico","situacaoEspecial","dataSituacaoEspecial","identificadorSocio","nomeSociorazaoSocial","cnpjcpfSocio","dataEntradaSociedade","dataSituacaoCadastral","nomeCidadeExterior","paisSocio","qualificacao_repre","nomeRepresentante","qualificacao_socio","faixaEtaria"]     
            frame= pd.DataFrame(a,columns=colunas)
            print(frame)
            frame.to_xml("pesquisa.xml")
         
               
                                
app()
