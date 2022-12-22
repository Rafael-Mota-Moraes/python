from dataclasses import dataclass, asdict, astuple

@dataclass()
class Pessoa:
    nome: str
    sobrenome: str
    idade: int = 0

    # def __init__(self, nome, sobrenome):
    #     self.nome = nome
    #     self.sobrenome = sobrenome
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    # def __post_init__(self):
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = sobrenome

if __name__ == '__main__':
    p1 = Pessoa('Rafael', 'Moreira')
    # p1.nome_completo = 'Rafael Mota'
    # print(p1.nome_completo)
    # print(astuple(p1))