produto = {
    'nome': 'Caneta',
    'preco': 2.5,
    'categoria': 'Escritório',
}

print(produto.items())

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

dc = {
    chave: valor
    for chave, valor in lista
}

s1 = {i for i in range(10) if i % 2 == 0}

print(dc)
print(s1)
