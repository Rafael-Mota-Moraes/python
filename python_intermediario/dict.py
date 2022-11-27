"""
'nome': 'Rafael',
'sobrenome': 'Moreira',
'idade': 18,
'altura': 1.8,
'enderecos': [
    { 'rua': 'tal tal', 'número': 123 },
    { 'rua': 'outra rua', 'número': 456 },
]
"""
pessoa = {}
chave = 'nome'
pessoa[chave] = 'Rafael'
pessoa['sobrenome'] = 'Moreira'

# print(pessoa, type(pessoa))
# print(pessoa['altura'])
# print(pessoa['nome'])
# print(pessoa['nomes'])

for chave in pessoa:
    print(f'{chave}: {pessoa[chave]}')

if pessoa.get('sobrenome', None) is None:
    print('Não existe!')

