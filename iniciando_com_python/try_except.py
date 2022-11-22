"""
Introdução ao try/except
try -> tentar executar o código
except -> Ocorreu algum erro ao tentar executar
"""

numero_str = input('Digite um número: ')

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.0f}')
except:
    print('Digite um número válido!')

