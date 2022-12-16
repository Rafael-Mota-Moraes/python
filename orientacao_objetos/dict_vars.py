class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade) :
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

p1 = Pessoa('Rafael', 18)
p2 = Pessoa('Helena', 35)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

print(p1.__dict__)
print(vars(p1))

