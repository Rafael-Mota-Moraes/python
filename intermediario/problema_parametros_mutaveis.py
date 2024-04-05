def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []

    lista.append(nome)
    return lista


lista1 = []
cliente1 = adiciona_clientes('Rafa', lista1)
adiciona_clientes('Joana', lista1)

print(cliente1)

lista2 = []
cliente2 = adiciona_clientes('Pedro', lista2)
adiciona_clientes('Marcelo', lista2)

print(cliente2)
