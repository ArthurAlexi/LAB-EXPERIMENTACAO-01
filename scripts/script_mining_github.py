# -*- coding: utf-8 -*-
"""Script_mining_github.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dQn2A09mLPAvbyt1fMwKQWh1Qr3Vuc2Y

# Setup

## Importações
"""

import requests as req
import pandas as pd
import json
from datetime import datetime
from google.colab import userdata

"""## Constantes"""

DOMAIN = 'https://api.github.com/graphql'
TOKEN = userdata.get('token')
HEADERS = {
  'Authorization': f'bearer {TOKEN}',
  'Content-Type': 'application/json'
}
TODAY = datetime.now()
NUMBER_OF_REPOSITORIES=1000

"""## Funções"""

def doPost(data : json)-> json:
  response = req.post(DOMAIN, headers=HEADERS, json=data)
  if response.status_code == 200:
    return response.json()

  raise Exception(f'Erro ao fazer requisição: {response.status_code} \n {response.text}')

def analisar_createdAt(repositorios):
  data_frame = pd.DataFrame(repositories)
  created_dates = [datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ') for date in data_frame['createdAt']]
  age_years = [round((TODAY - date).days / 365, 2) for date in created_dates]
  return age_years
  # data_frame['Age (Years)'] = age_years
  # return  data_frame

def tratar_updateAt(repositories):
  data_frame = pd.DataFrame(repositories)
  updated_dates = [datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ') for date in data_frame['createdAt']]
  days = [round((TODAY - date).days, 2) for date in updated_dates]
  return days

def analisar_issues_fechadas(repositorios):
    lista = []
    for repo in repositorios:
        total_issues = repo.get('issues', {}).get('totalCount', 0)
        total_issues_fechadas = repo.get('closedIssues', {}).get('totalCount', 0)
        percentual_issues_fechadas = (total_issues_fechadas / total_issues) * 100 if total_issues > 0 else 0
        lista.append(round(percentual_issues_fechadas,2))

    return lista

"""## Query Geral"""

query_template = """
query search_repositories($queryString: String!, $perPage: Int!, $cursor: String) {
  search(query: $queryString type: REPOSITORY, first: $perPage, after: $cursor) {
    repositoryCount
    edges {
      node {
        ... on Repository {
          nameWithOwner
          updatedAt
          createdAt
          releases {
            totalCount
          }
          issues {
            totalCount
          }
          closedIssues: issues(states: CLOSED) {
            totalCount
          }
          openIssues: issues(states: OPEN) {
            totalCount
          }
          primaryLanguage {
            name
          }
          pullRequests(states: MERGED) {
            totalCount
          }
        }
      }
    }
    pageInfo {
      endCursor
      hasNextPage
    }
  }
}
"""


per_page = 20
cursor = None
query_string = "stars:>{0}".format(NUMBER_OF_REPOSITORIES)
repositories = []

while len(repositories) < NUMBER_OF_REPOSITORIES:
    variables = {
        "queryString": query_string,
        "perPage": per_page,
        "cursor": cursor
    }
    data = doPost(data={'query': query_template, 'variables': variables})

    if 'errors' in data:
        print("GraphQL query failed:", data['errors'])
        break

    for edge in data['data']['search']['edges']:
        repositories.append(edge['node'])

    if data['data']['search']['pageInfo']['hasNextPage']:
        cursor = data['data']['search']['pageInfo']['endCursor']
    else:
        break

print("Total repositories: ", len(repositories))
print("Cursor: ", cursor)
print("Per page: ", per_page)

# data_brutus = pd.DataFrame(repositories)
# data_brutus.to_csv('dados_base.csv', index=False, sep=';')

"""## Tratamento"""

dataFrame_tratado = pd.DataFrame()
dataFrame_tratado['Repositorio'] = [repo.get('nameWithOwner') for repo in repositories]
dataFrame_tratado['Anos'] = analisar_createdAt(repositories)
dataFrame_tratado['nº PullRequests'] = [repo.get('pullRequests', {}).get('totalCount', 0) if isinstance(repo, dict) else 0 for repo in repositories]
dataFrame_tratado['nº Releases'] = [repo.get('releases').get('totalCount',0) if isinstance(repo, dict) else 0 for repo in repositories]
dataFrame_tratado['Último Update (dd)'] = tratar_updateAt(repositories)
dataFrame_tratado['Linguagem Mais Comum'] = [repo.get('primaryLanguage', {}).get('name', None) if (isinstance(repo, dict) and repo.get('primaryLanguage') is not None) else None for repo in repositories]
dataFrame_tratado['Issues Fechadas ( % )'] = analisar_issues_fechadas(repositories)

dataFrame_tratado.head()

# dataFrame_tratado.to_csv('dados_tratados.csv', index=False, sep=';')

"""# Hipóteses Informais:

### RQ 01: Sistemas populares são maduros/antigos?

<strong>Hipótese informal:</strong> Sistemas populares tendem a ser mais antigos, uma vez que a maturidade e a popularidade geralmente exigem tempo para se desenvolverem.

### RQ 02: Sistemas populares recebem muita contribuição externa?

<strong>Hipótese informal:</strong> Sistemas populares geralmente recebem uma quantidade significativa de contribuições externas, pois a popularidade tende a atrair uma comunidade maior de desenvolvedores interessados em colaborar. Porém, nem todas as contribuições são aceitas.

### RQ 03: Sistemas populares lançam releases com frequência?

<strong>Hipótese informal:</strong> Sistemas populares tendem a lançar releases com frequência, já que uma comunidade ativa muitas vezes busca novas funcionalidades e correções de bugs regularmente.

### RQ 04: Sistemas populares são atualizados com frequência?

<strong>Hipótese informal:</strong> Sistemas populares são frequentemente atualizados, pois a manutenção contínua é necessária para sustentar sua popularidade e atender às demandas da comunidade.

### RQ 05: Sistemas populares são escritos nas linguagens mais populares?

<strong>Hipótese informal:</strong> Sistemas populares têm uma tendência a serem escritos nas linguagens de programação mais populares, uma vez que isso pode aumentar sua acessibilidade e atratividade para uma base de desenvolvedores mais ampla.

### RQ 06: Sistemas populares possuem um alto percentual de issues fechadas?

<strong>Hipótese informal:</strong> Sistemas populares tendem a ter um alto percentual de issues fechadas. Por dois fatores: esses sistemas possuem comunidade maior que  geralmente implica em uma capacidade maior de resolver problemas e responder às necessidades dos usuários. E o outro fator é devido a complexidade e tamanho do sistema, tornando-se comum ter bugs e issues sendo fechadas.

# Análises

## RQ 01: Sistemas populares são maduros/antigos?
### Métrica: idade do repositório (calculado a partir da data de sua criação)
"""



"""## RQ 02: Sistemas populares recebem muita contribuição externa?
### Métrica: total de pull requests aceitas
"""



"""## RQ 03: Sistemas populares lançam releases com frequência?
### Métrica: total de releases
"""



"""## RQ 04: Sistemas populares são atualizados com frequência?
### Métrica: tempo até a última atualização (calculado a partir da data de última atualização)
"""



"""## RQ 05: Sistemas populares são escritos nas <a href='https://octoverse.github.com/'>linguagens mais populares</a>?

### Métrica: linguagem primária de cada um desses repositórios
"""



"""## RQ 06: Sistemas populares possuem um alto percentual de issues fechadas?
### Métrica: Métrica: razão entre número de issues fechadas pelo total de issues)

# Lembrete @ Plabo @Charut

### na query tem a gente ta pegando o updateAt mas isso só retorna a ultima atualização do github em cima do repositório, temos q ver onde busca a ultima atualização de commit, merge ou sla do repo
"""