class Animal:
    # nome = 'Leão'

    def __init__(self, nome):
        self.nome = nome
        variavel = 'Interna no método init'
        print(variavel)

    def acao(self):
        return f'{self.nome} está executando uma ação.'


leao = Animal('Leão')
print(leao.nome)
print(leao.acao())
