# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações
# Por convenç]ao, usamos PascalCase para nomes de classes.

# classe str gerou a instancia "string"
string = 'Rafa'  # str
print(string.upper())
print(isinstance(string, str))


class Pessoa:
    ...


p1 = Pessoa()
p1.nome = 'Rafa'
p1.sobrenome = 'Moreira'
print(p1.nome)
print(p1.sobrenome)

p2 = Pessoa()
p2.nome = 'João'
p2.sobrenome = 'Silva'
print(p2.nome)
print(p2.sobrenome)
