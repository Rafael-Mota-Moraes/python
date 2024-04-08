# @property + @setter - getter e setter

class Caneta:
    def __init__(self, cor) -> None:
        self._cor = cor

    @property
    def cor(self):
        print('PROPERTY')
        return self._cor

    @cor.setter
    def cor(self, valor):
        self._cor = valor


caneta = Caneta('Azul')
caneta.cor = 'Rosa'
print(caneta.cor)
