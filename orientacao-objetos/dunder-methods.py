# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str

class Ponto:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'(x={self.x}, y={self.y})'

    def __repr__(self) -> str:
        return f'{__class__.__name__}({self.x}, {self.y})'

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y

        return Ponto(novo_x, novo_y)

    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y

        return resultado_self > resultado_other


p1 = Ponto(1, 2)
p2 = Ponto(900, 1000)
p3 = p1 + p2


print(p1)
print(f'{p2!r}')
print(f'{p2!s}')
print(p3)
print('P1 é maior que p2?', p1 > p2)
