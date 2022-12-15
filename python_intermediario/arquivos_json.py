import json

# pessoa = {
#     'nome': 'Rafael',
#     'sobrenome': 'Moreira',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

# with open('pessoa.json', 'w', encoding='utf-8') as arquivo:
#   json.dump(pessoa, arquivo, indent=2)

with open('pessoa.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)