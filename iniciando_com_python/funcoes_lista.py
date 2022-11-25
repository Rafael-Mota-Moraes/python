lista_c = [1, 2, 3, 4]
# numero = lista[2]
# # print(numero)

lista_c[2] = 300
del lista_c[1]

lista_c.append(5)
lista_c.append(6)
lista_c.pop()
lista_c.append(7)
lista_c.pop(1)

lista_c.append('Rafael')

nome = lista_c.pop()
del lista_c[-1]
# lista.clear()
lista_c.insert(0, 'valor adicionado no insert')
lista_c.insert(600000, 'segundo valor adicionado no insert')

# print(lista)
# print(lista[1])
# print(nome)

lista_a = [1, 2, 3, 4, 5]
lista_b = [6, 7, 8, 9, 10]

lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)
print(lista_d)
