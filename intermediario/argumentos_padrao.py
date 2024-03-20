"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem ter valores padrão. Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.
"""


def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} + {y=} + {z=} = {x + y + z}')
    else:
        print(f'{x=} + {y=} = {x + y}')


soma(1, 1, 1)
soma(2, 2)
soma(y=10, z=5, x=3)
