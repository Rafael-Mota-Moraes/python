"""
Listas m Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

string = 'ABCDE' #5 caracteres
lista = list(['item 1', 'item 2', 'item 3'])
print(bool([]))
print('1) ', lista)
lista = ['item 1', 'item 2', 'item 3']
print('2) ', lista)
lista[1] = 'novo item'
print('3) ', lista)

lista_complexa = [1, 2, 3, ['Rafael', 'João', 'mária'], [[4, 5, 6], [7, 8, 9]]]
print('4)', lista_complexa)
print(lista_complexa[4][0][1])