class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Rafael', 'Moreira')
print(p1.nome)
print(p1.sobrenome)
