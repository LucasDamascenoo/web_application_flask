#pip install plotly, requests
#https://plotly.com/python/basic-charts/

import csv
import requests
from contextlib import closing


respiradores_url_dados = 'https://sage.saude.gov.br/dados/repositorio/distribuicao_respiradores.csv'
dados = []

with closing(requests.get(respiradores_url_dados, stream=True)) as r:
    f = (line.decode('utf-8') for line in r.iter_lines())
    reader = csv.reader(f, delimiter=';', quotechar='"')
    for row in reader:
        dados.append(row)

cabecalho = dados[0]
dados = dados
print('cabecalho', dados[0])

def coluna(chave=-1):
    return cabecalho.index(chave)

def filtrar(dados, nome_coluna, valor):
    return [dado for dado in dados if(dado[coluna(nome_coluna)]==valor)]

def selecionar(dados, nome_coluna):
    return [dado[coluna(nome_coluna)] for dado in dados]

dados_rgn = filtrar(dados, 'DESTINO', 'RIO GRANDE DO NORTE')
dados_rgn_mun = filtrar(dados_rgn, 'TIPO', 'UTI')
x = selecionar(dados_rgn_mun, 'DATA')
y = selecionar(dados_rgn_mun, 'QUANTIDADE')



import plotly.graph_objects as go

fig = go.Figure(go.Scatter(x=x, y=y, name='QTDE'))

fig.update_layout(title='Respiradores',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)
fig.write_image('teste.png')
