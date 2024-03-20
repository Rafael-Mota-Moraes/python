# desempacotamento
x, y, *resto = 1, 2, 3, 4

print(x, y, resto)


# def soma(x, y):
#     return x + y


def soma(*args):
    args = list(args)
    soma = 0

    for numero in args:
        soma += numero

    return soma


numeros = 1, 2, 3, 4, 5
minha_soma = soma(*numeros)
print(minha_soma)
print(sum((1, 2, 3, 4, 5)))
