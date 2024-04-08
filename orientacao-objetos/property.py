# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# modo pythônico - modo do Python de fazer as coisas
# @property é uma propriedade do objeto, ela é um metodo que se comporta como um atributo

# Geralmente é usada nas seguintes situações:
#  - Como getter
#  - p/ evitar quebrar código cliente
#  - p/ habilitar setter
#  - p/ executar ações ao obter um atributo

class Caneta:
    def __init__(self, cor) -> None:
        self.cor = cor

    @property
    def get_cor(self):
        return 'qualquer coisa'


caneta = Caneta('Azul')
print(caneta.get_cor)
