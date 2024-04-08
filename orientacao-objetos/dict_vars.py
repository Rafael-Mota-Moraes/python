class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados)
# p1.nome = 'Outro João'
# print(p1.idade)
# p1.__dict__['outra'] = 'coisa'
print(p1.__dict__)
print(vars(p1))
