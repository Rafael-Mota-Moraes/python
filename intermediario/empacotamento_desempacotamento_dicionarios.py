# Empacotamento e desempacotamento em dicionários
a, b = 1, 2
a, b = b, a

pessoa = {
    'nome': 'Rafael',
    'sobrenome': 'Moreira',
}

a, b = pessoa.values()
print(a, b)

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

for chave, valor in pessoa.items():
    print(chave, valor)

dados_pessoa = {
    'idade': 16,
    'altura': 1.65
}

pessoa_completa = {**pessoa, **dados_pessoa}

print(pessoa_completa)


def mostro_argumentos_nomeados(*args, **kwargs):
    print(kwargs)


mostro_argumentos_nomeados(nome="Rafael", numero=123)
mostro_argumentos_nomeados(**pessoa_completa)
