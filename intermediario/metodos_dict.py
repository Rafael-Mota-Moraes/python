import copy

pessoa = {
    'nome': 'Rafael',
    'sobrenome': 'Moreira',
    # 'idade': 19
}

print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

print()

for chave in pessoa.keys():
    print(chave)

print()

for chave, valor in pessoa.items():
    print(chave, valor)

print()

pessoa.setdefault('idade', None)
print(pessoa['idade'])

# Shallow copy e deep copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [1, 2, 3]
}

d2 = d1

d2 = copy.deepcopy(d1)

d2['c1'] = 100
d2['l1'][1] = 10
print(d1)
print(d2)

print()

print(pessoa.get('nome'))

nome = pessoa.pop('nome')
print(nome)

pessoa['nome'] = 'Rafael'
ultima_chave = pessoa.popitem()

print(ultima_chave)
pessoa['nome'] = 'Rafael'
pessoa.update({
    'idade': 19
})

print(pessoa)
