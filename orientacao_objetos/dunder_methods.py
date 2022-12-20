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


p1 = Ponto(1, 2)
p2= Ponto(134, 1223)

print(p1)
print(p2)
