class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta

    @property
    def cor_tampa(self):
        return f'A caneta tem uma tampa {self.cor_tinta}'


caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor_tampa)

