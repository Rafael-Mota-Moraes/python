class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)



class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('Apagando: ', self.rua, self.numero)

cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av. Brasil', 34)
cliente1.inserir_endereco('Rua B', 472)

cliente1.listar_enderecos()