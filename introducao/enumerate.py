"""
enumerate = enumera iteráveis (índices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = enumerate(lista)
print(lista)
print(tuple(lista_enumerada))

for item in lista_enumerada:
    print(item)

print()

for item in enumerate(lista):
    print(item)
