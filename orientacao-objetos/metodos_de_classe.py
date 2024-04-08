# Métodos de classe + factories
# São métodos onde "self" será "cls", ou seja, ao invés de receber a instância no primeiro parâmetro, recebemos a própria classe.

class Pessoa:
    ano = 2023  # atributos de classe

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


p1 = Pessoa('João', 18)
p2 = Pessoa.criar_com_50_anos('Pedro')
p3 = Pessoa.criar_sem_nome(18)

print(p2.nome)
print(p2.idade)

print(p3.nome)
print(p3.idade)
