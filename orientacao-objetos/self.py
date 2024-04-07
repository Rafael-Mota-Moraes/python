# Entendendo o self

class Carro:
    def __init__(cls, nome):  # self é uma convenção!
        cls.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
Carro.acelerar(fusca)
fusca.acelerar()
print(fusca.nome)

celta = Carro('Celta')
celta.acelerar()
print(celta.nome)
