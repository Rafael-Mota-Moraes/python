produto = {
    'nome' : 'Caneta Azul',
    'preco' : 2.5,
    'categoria': 'Escritório'
}

for chave, valor in produto.items():
    # print(chave, valor)
    ...

dc = {
    chave: valor
    if isinstance(valor, (float, int)) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
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

print(dc)
