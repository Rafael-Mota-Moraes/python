class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Olá mundo')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('José')

print(Pessoa.ano)
# p1.metodo_de_classe()
Pessoa.metodo_de_classe()
print(p2.nome, p2.idade)
