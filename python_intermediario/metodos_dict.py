# pessoa = {
#     'nome': 'Rafael',
#     'sobrenome': 'Pereira',
#     'idade': 90
# }

# pessoa.setdefault('idade', None)
# print(pessoa['idade'])

# print(len(pessoa))
# print(list(pessoa.keys()))

# for chave in pessoa.keys():
#     print(chave)
# import copy


# d1 = {
#     'c1': 1, 
#     'c2': 2,
#     'l1': [0, 1, 2]
# }


# d2 = copy.deepcopy(d1)

# d2['c1'] = 30000
# print(d1)

p1 = {
    'nome': 'Rafael',
    'sobrenome': 'Pereira',
}

print(p1.get('nome'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

sobrenome = p1.popitem()
print(sobrenome)

p1.update({
    'idade': 34
})

p1.update(nome='Novo Nome')

print(p1)
