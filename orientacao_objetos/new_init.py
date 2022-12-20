
class A:
    def __new__(cls):
        print('Antes de criar a instância')
        return super().__new__(cls)

    def __init__(self):
        print(self)

    def __repr__(self) -> str:
        return f'A()'


# a = object.__new__(A)
# a.__init__()
a = A()

print(a)
