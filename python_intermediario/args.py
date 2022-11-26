# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

def soma(*args): 
    total = 0

    for numero in args:
        total += numero

    return total

numeros = 1, 2, 3, 4, 5
soma_total = soma(*numeros)
print(soma_total)