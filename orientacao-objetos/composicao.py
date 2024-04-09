# Composição é uma especialização da agregação
# Mas nela, quando o objeto "pai" for apagado, todas as referências dos objetos filhos também são apagadas

class Cliente:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('Apagando: ', self.nome)


class Endereco:
    def __init__(self, rua, numero) -> None:
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('Apagando: ', self.rua, self.numero)


cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av Principal', 10)
cliente1.inserir_endereco('Rua Secundaria', 12)
cliente1.listar_enderecos()
print('Código termina aqui')
