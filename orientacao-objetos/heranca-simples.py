# Herança simples - Relações entre classes
# Associação - usa, agregação - tem
# Composição - É dono de, Herança - É um

# Herança ou composição

# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

# object
class Pessoa:
    cpf = '1234'

    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    ...


class Aluno(Pessoa):
    cpf = '4321'


c1 = Cliente('Rafael', 'Moreira')
c1.falar_nome_classe()
a1 = Aluno('João', 'Silva')
a1.falar_nome_classe()

print(c1.cpf)
print(a1.cpf)
# help(Cliente)
