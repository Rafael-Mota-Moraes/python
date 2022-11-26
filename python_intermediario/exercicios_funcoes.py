# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    total_da_multiplicacao = 1
    for arg in args:
        total_da_multiplicacao *= arg

    return total_da_multiplicacao

print(multiplica(1,2,3,4))

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def e_par(numero):
    if numero % 2 == 0:
        return f'Número: {numero} é par.'
    else:
        return f'Número: {numero} é impar.'


print(e_par(2))
print(e_par(5))
