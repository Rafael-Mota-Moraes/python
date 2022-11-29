lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def ordena(item):
#     return item['nome']

# ordena = lambda item: item['nome']

# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(key=ordena)

# for item in lista:
#     print(item)


def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador

    return multiplica

duplica = executa(
    lambda m: lambda n: n*m,
    2
)

print(duplica(2))

print(
    executa(
        lambda x, y: x + y, 2, 3
    ),
    executa(soma, 2, 3)
)
