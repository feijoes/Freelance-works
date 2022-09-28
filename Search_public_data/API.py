import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
    return "API on"

@app.route('/')
def infos():
    tabela = pd.read_csv('planilhe.csv')
    total_vendas = tabela['vendas'].sum()
    resposta = {'total_vendas': total_vendas}
    return jsonify(resposta)

app.run()