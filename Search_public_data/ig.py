import PySimpleGUI as sg

def app():

    sg.theme('Dark Grey 13')
    
    # INPUTS:
    # rs - Razao Social          # CEP -CEP                               # cnpj - CNPJ Basico -- adicionar
    # CNAE - Atvidade Principal  # DDD - DDD                              # ql - Qualificaçao do responsável --adicionar
    # NJ - Natural Juridica      # datade - Data de abertura  a partir    # efr - Ente federativo responsavel -- adicionar
    # UF - Estado                # dataate - Data de abertura ate
    # mn - Municipio             # apartir - Capital Social a partir
    # bairro - bairro            # ate - Capital social ate

    layout = [
        [sg.Text("Razão social ou nome fantasia:"), sg.Input(key="rs"), sg.Text("Atividade Principal (CNAE):"), sg.Input(key="cnae.descricao")],
        [sg.Checkbox("Incluir Atividade Secundária", key="ias")],
        [sg.Text("Natureza Jurídica: "), sg.Input(key="naturezajuridico.descricao")],
        [sg.Text("Situação cadastral: "), sg.Combo(['NULA', 'ATIVA', 'SUSPENSA', 'INAPTA', 'BAIXADA'])],
        [sg.Text("Estado (UF)"), sg.Input(key="uf", size=(3, 1)), sg.Text("Municipio"), sg.Input(key="municipio.descrisao")],
        [sg.Text("Bairro"), sg.Input(key="Bairro"), sg.Text("CEP"), sg.Input(key="CEP", size=(15, 1)), sg.Text("DDD - 2 digitos"), sg.Input(key="DDD", size=(2,1))],
        [sg.Text("Data de abertura - A partir de"), sg.Input(key="socio.dataOpcao"), sg.Text("Data de abertura - Até"), sg.Input(key="dataate")],
        [sg.Text("Capital Social - A partir de"), sg.Input(key="apartir"), sg.Text("Capital Social - Ate"), sg.Input(key="ate")],
        [sg.Checkbox("Somente mei", key="sm"), sg.Checkbox("Excluir MEI", key="em"), sg.Checkbox("Somente Matriz", key="sma"), sg.Checkbox("Somente fixo", key="sf")],
        [sg.Checkbox("Somente filial", key="sfl"), sg.Checkbox("Com contato de telefone", key="st"), sg.Checkbox("Somente celular", key="sc")],
        [sg.Checkbox("Com e-mail", key="ce")],
        [sg.Button("PESQUISAR", size=(20, 2)), sg.Button("BUSCA SIMPLIFICADA", size=(20, 2))],
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
            sg.popup_yes_no("teste")
        elif evento == "PESQUISAR":
            # pegando todos os dados:
            razao, atividade, natural, estado, municipio, bairro, cep, ddd, datade, dataate, apartir, ate = valores["rs"], valores['CNAE'], valores['NJ'], valores['UF'], valores['mn'], valores['Bairro'], valores['CEP'], valores['DDD'], valores['datade'], valores['dataate'], valores['apartir'], valores['ate']
            print(razao, atividade, natural, estado, municipio, bairro, cep, ddd, datade, dataate, apartir, ate)
            # transformando todos os valores em apenas uma string
            all_valores = valores["ias"], valores["sm"], valores["em"], valores["sma"], valores["sf"], valores["sfl"], valores["st"], valores["sc"], valores["ce"]
            
            """
            c = {f'pais.descricao': '{estado}', 'municipio.descricao': '{municipio}'}
            dados = 'select cnpjBasico, porte,nomeSocial, naturezajuridico.descricao, qualificacao.descricao, capital, porte, responsavel iner join'

            for chave, valor in c:
                a += f'where {chave} ="{valor.upper()}" and'
                a[:-3]
            """
app()