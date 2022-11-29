a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    'nome': 'Rafael',
    'sobrenome': 'Moreira'
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6
}


pessoa_completa = { **pessoa, **dados_pessoa }

print(pessoa_completa)
(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

for chave, valor in pessoa.items():
    print('For:', chave, valor)


def mostro_argumentos_nomeados(*args, **kwargs):
    print(kwargs)


mostro_argumentos_nomeados(nome='Rafael', idade=17)
