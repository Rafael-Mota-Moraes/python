# Escopo da classe e de métodos da classe
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
        variavel = 'valor'
        print(variavel)

    def acao(self):
        print(f'{self.nome} está executando uma ação...')

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


leao = Animal(nome='Leão')
print(leao.nome)
leao.acao()
print(leao.executar('planta'))
