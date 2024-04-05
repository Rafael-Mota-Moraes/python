import json

# pessoa = {
#     'nome': 'Rafael',
#     'sobrenome': 'Moreira',
#     'enderecos': [
#         {'rua': 'Av. Principal', 'numero': 55},
#         {'rua': 'Av. Secundária', 'numero': 44},
#     ],
#     'altura': 1.7,
#     'numeros_preferidos': (5, 10, 15, 20),
#     'dev': True,
#     'nada': None
# }

# with open('./intermediario/json.json', 'w') as arquivo:
#     json.dump(pessoa, arquivo, indent=2)


with open('./intermediario/json.json', 'r') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa))
