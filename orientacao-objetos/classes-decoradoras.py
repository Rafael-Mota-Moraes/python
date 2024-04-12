class Multiplicar:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


@Multiplicar
def soma(x, y):
    return x + y


dois_mais_dois = soma(2, 2)
print(dois_mais_dois)
