
class Carro:
    def __init__(self, nome, delta_velocidade):
        self.nome = nome
        self.velocidade = 0
        self.delta_velocidade = delta_velocidade

    def acelerar(self):
        self.velocidade += self.delta_velocidade

    def get_velocidade(self):
        return f'{self.velocidade}Km/h'


fusca = Carro('Fusca', 10)
fusca.acelerar()
fusca.acelerar()
fusca.acelerar()
print(fusca.nome)
print(fusca.get_velocidade())
