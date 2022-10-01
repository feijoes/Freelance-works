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
        [sg.Text("Natureza Jurídica: "), sg.Input(key="natureza_juridico_Empresa.descricao")],
        [sg.Text("Situação cadastral: "), sg.Combo(['NULA', 'ATIVA', 'SUSPENSA', 'INAPTA', 'BAIXADA'])],
        [sg.Text("Estado (UF)"), sg.Input(key="estabelecimentos.uf", size=(3, 1)), sg.Text("Municipio"), sg.Input(key="municipio.descricao")],
        [sg.Text("Bairro"), sg.Input(key="estabelecimentos.bairro"), sg.Text("CEP"), sg.Input(key="estabelecimentos.cep", size=(15, 1)), sg.Text("DDD - 2 digitos"), sg.Input(key="estabelecimentos.ddd1", size=(2,1))],
        [sg.Text("Data de abertura - A partir de"), sg.Input(key="socio.dataOpcao"), sg.Text("Data de abertura - Até"), sg.Input(key="dataate")],
        [sg.Text("Capital Social - A partir de"), sg.Input(key="empresas.capital"), sg.Text("Capital Social - Ate"), sg.Input(key="ate")],
        [sg.Checkbox("Somente mei", key="sm"), sg.Checkbox("Excluir MEI", key="em"), sg.Checkbox("Somente Matriz", key="simples.opcaoMei"), sg.Checkbox("Somente fixo", key="sf")],
        [sg.Checkbox("Somente filial", key="sfl"), sg.Checkbox("Com contato de telefone", key="estabelecimentos.telefone1"), sg.Checkbox("Somente celular", key="sc")],
        [sg.Checkbox("Com e-mail", key="estabelecimentos.correioEletronico")],
        [sg.Button("PESQUISAR", size=(20, 2))],
        [sg.Text("", key="response")]
        ]

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
        elif evento == "PESQUISAR":
            # pegando todos os dados:
            example = """
            select empresas.cnpjBasico
            ,public.empresas.nomeSocial
            ,public.naturezajuridico.descricao natureza_juridico_Empresa
            ,qualificacao_Empresa.descricao empresa_qualificacao
            ,empresas.capital
            ,empresas.porte,
             public.empresas.responsavel
            ,public.estabelecimentos.cnpjOrdem
            ,public.estabelecimentos.cnpjDv, 
            public.estabelecimentos.matriz,
             public.estabelecimentos.nomeFantasia, 
             public.estabelecimentos.situacaoCadastral
             ,public.estabelecimentos.dataSituacaoCadastral
             , public.estabelecimentos.nomeCidadeExterior
             , estabelecimento_pais.descricao estabelecimento_Pais
             , public.estabelecimentos.dataAtividade
             , cnae_principal.descricao cnae_principal
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
             where 
             """
            for chave,valor in valores.items():
                num = 1
                if num:
                    num-=1
                    if valor:
                        example+= f'{chave} like "%{valor}%"'
                else:
                    if valor:
                        example+= f' and {chave} like "%{valor}%"'
            cursor.execute(example)
            a= cursor.fetchall()
            print(a)
            
                    
                    
                                
app()
