"""
Argumentos nomeados e não nomesdos em funções Python
Argumentos nomeados tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y):
    # Definição
    print(f'{x=} | {y=}')
    print(f'{x} + {y} = {x + y}')


soma(1, 1)
soma(y=2, x=2)
print(soma)
