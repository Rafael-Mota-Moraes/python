import modularizacao_modulo
from modularizacao_modulo import variavel_modulo

import importlib

import sys
sys.path.append('/home')

for i in range(10):
    importlib.reload(modularizacao_modulo)

print('Este módulo de chama: ', __name__)
# print(*sys.path, sep='\n')
print(variavel_modulo)
