import requests
import json
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import logging

# ATENÇÃO: para o código funcionar, coloque a sua chave de acesso ao Portal da Transparencia no local indicado.

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_request(url_):
  headers = {"chave-api-dados" : "COLOQUE SUA CHAVE"}
  resposta = requests.get(url_, headers=headers)
  return resposta.json()
  
def coletar_dados(url):
  logging.info('Pegou URL para a criação das diferentes URLs criando uma para cada página')
  list_urls = [url + str(i) for i in range(1, 6)]
  arr_urls = np.asarray(list_urls)

  vec_run = np.vectorize(run_request)
  logging.info('Fazendo uma requisição para cada URL')
  arr_responses = vec_run(arr_urls)
  logging.info('Requisições concluídas')
  arr_responses = arr_responses.tolist()
  reposta = np.concatenate(arr_responses).tolist()
  return reposta

def transformar_dado(dado):
  logging.info('Criando dataframe')
  # Insira o código para a criação do dataframe a partir do parâmetro 'dado'
  df = pd.DataFrame(dado)
  # A variável deve ter o nome df_area
  # Insita o log sobre o que está sendo executado, utilizando 'logging.info'
  logging.info('Selecionando Colunas')
  df_area = df[['funcao', 'valorEmpenhado']]

  # Insita o log sobre o que está sendo executado, utilizando 'logging.info'
  logging.info('Transformando dado String -> Float')
  df_area['valorEmpenhado'] = df_area['valorEmpenhado'].str.replace('.', '').str.replace(',', '.').astype(np.float64)

  logging.info('Transformando dado string -> float')
  agg_area = df_area.groupby('funcao').sum('valorEmpenhado')

  logging.info('Transformando dados para retirar proporção em porcentagem')
  agg_area = agg_area['valorEmpenhado']/df_area['valorEmpenhado'].sum()

  # Insira o código para reset de index de agg_area, usando reset_index()
  agg_are = agg_area.reset_index()

  return agg_area

def carga(dado):
    logging.info('Salvando arquivo...')
    dado.to_csv('distribuicao_empenho_area_2022.csv')
    logging.info('Arquivo salvo')

def etl():
  logging.info('ETL iniciada...')
  url = 'https://api.portaldatransparencia.gov.br/api-de-dados/emendas?ano=2022&pagina='
  # colete os dados
  dado = coletar_dados(url)
  # transforme os dados
  dado = transformar_dado(dado)
  # salve os dados
  carga(dado)
  logging.info('ETL finalizada!')

etl()