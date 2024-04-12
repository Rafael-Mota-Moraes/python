# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e retornar o novo objeto. Por isso, new recebe cls.
# __new__ DEVE retornar o novo objeto
# __init__ é o método responsável por inicializar a instância. Por isso, init recebe self.
# __init__ NÃO DEVE retornar nada

class A:
    def __new__(cls, *args, **kwargs):
        print('Antes de criar a instância...')
        instancia = super().__new__(cls)
        print('Antes de criar a instância...')
        instancia.x = 123
        print('X vale:', instancia.x)
        return instancia

    def __init__(self, x) -> None:
        self.x = x
        print(self)

    def __repr__(self) -> str:
        return f'A()'


a = A()

# a = object.__new__(A)
# a.__init__()
# print(a)
