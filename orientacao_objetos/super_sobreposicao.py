# class MinhaString(str):
#     def upper(self):
#         print('Chamou upper')
#         retorno = super().upper()
#         print('Depois do upper')
#         return retorno


# string = MinhaString('rafa')
# print(string.upper())

class A:
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def metodo(self):
        # super(B, self).metodo()
        # super(C, self).metodo()
        print('C')

c = C('atributo', 'qualquer')
print(c.atributo)
print(c.outra_coisa)
print(C.mro())
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()
