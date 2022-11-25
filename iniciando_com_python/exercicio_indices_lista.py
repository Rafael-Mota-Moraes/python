"""
Exercício
Exiba os índices da lista
"""

lista = ['Maria', 'Helena', 'Luiz']

for nome in lista:
    index = lista.index(nome)
    print(f'{nome}: {index}')
