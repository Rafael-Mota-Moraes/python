string = 'Rafael' # tipo = str

# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Rafael', 'Moreira')

print(p1.nome)
print(p1.sobrenome)
