import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'csv.csv'
CAMINHO_CSV2 = Path(__file__).parent / 'csv2.csv'

# with open(CAMINHO_CSV, 'r') as arquivo:
#     leitor = csv.reader(arquivo)

#     for linha in leitor:
#         print(linha)


lista_clientes = [
    {'Nome': 'Rafael', 'Idade': '19', 'Endereco': 'Av Brasil, 21,Centro'},
    {'Nome': 'Pedro', 'Idade': '22', 'Endereco': 'Av Brasil, 50,Centro'}
]

with open(CAMINHO_CSV, 'r', encoding='utf8', newline='') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        # print(linha)
        ...

with open(CAMINHO_CSV2, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.writer(arquivo)

    escritor.writerow(nome_colunas)

    for cliente in lista_clientes:
        escritor.writerow(cliente.values())
