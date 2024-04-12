# Método especial __call__
# Callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma classe "callable"

class CallMe:
    def __init__(self, phone) -> None:
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'está chamando', self.phone)


call1 = CallMe('2321984901')
call1('Rafa')
