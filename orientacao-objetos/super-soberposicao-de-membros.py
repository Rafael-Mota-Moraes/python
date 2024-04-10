# super() é a super classe na sub classe

class MinhaString(str):
    def upper(self):
        print('chamou upper')
        return super().upper()


# nome = MinhaString('Rafa')

# print(nome.upper())

class A(object):
    atributo_a = 'A'

    def __init__(self, atributo) -> None:
        self.atributo = atributo

    def metodo(self):
        print('M A')


class B(A):
    atributo_b = 'B'

    def metodo(self):
        super(B, self).metodo()
        print('M B')


class C(B):
    atributo_c = 'C'

    def metodo(self):
        super(C, self).metodo()
        print('M C')


c = C('atributo')

# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()

print(C.mro())
print(c.atributo)
