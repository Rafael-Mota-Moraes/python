def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


duplica = executa(
    lambda m: lambda n: m * n, 2
)

print(executa(lambda x, y: x + y, 1, 1))
print(duplica(3))
