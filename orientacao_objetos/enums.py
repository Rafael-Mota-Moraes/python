import enum
from enum import Enum

# Direcoes = Enum('Direcoes', ['ESQUERDA', 'DIREITA'])

class Direcoes(Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()


print(Direcoes(1), Direcoes['ESQUERDA'].name, Direcoes.ESQUERDA.value)

def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada!')
    print(f'Movendo para {direcao.name}')

# mover('esquerda')
# mover('direita')
mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)