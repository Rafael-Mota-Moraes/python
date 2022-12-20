class Ponto:
    def __init__(self, x, y, z='String') -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x!r}, {self.y!r}, {self.z!r})'

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}(x={self.x}, y={self.y})'

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        
        return Ponto(novo_x, novo_y)

    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        
        return resultado_self > resultado_other
        


p1 = Ponto(1, 2)
p2 = Ponto(1, 2)
p3 = p1 + p2

print(p1)
print(p2)
print(p3)
print('p1 > p2', p1 > p2)
