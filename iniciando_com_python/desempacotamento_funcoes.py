string = 'ABCD'
lista = ['Maria', 'Helena',1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal.'

a, b, *_, u  = lista
print(a, u)

# for nome in lista:
#     print(nome, end=' ', sep=' ')

print(*lista)
