# dataclasses
# O módulo dataclasses fornece um decorador e funções para criar métodos como __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais

from dataclasses import dataclass, asdict, astuple


@dataclass(init=False)
class Pessoa:
    nome: str
    sobrenome: str
    idade: int = 19  # valor padrão só funciona para valores imutáveis

    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa('Rafael', 'Moreira')

    print(p1.nome_completo)
    print(asdict(p1))
    print(astuple(p1))
