pessoa = {}


chave = 'nome'
pessoa[chave] = 'Rafael'
pessoa['sobrenome'] = 'Moreira'


print(pessoa['nome'])
print(pessoa[chave])
print(pessoa)
del pessoa['sobrenome']
print(pessoa)
# print(pessoa['outra_chave']) levanta uma excessão!


if pessoa.get('sobrenome') is None:
    print('Chave não existe!')
else:
    print(pessoa['sobrenome'])
