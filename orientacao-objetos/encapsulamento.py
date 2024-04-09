# Encapsulamento (modificadores de acesso: public, protected e private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
#   _ (um underline) = protected
#       não deve ser usado fora da classe ou suas subclasses.
#   __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python só DEVE ser usado na classe em que foi declarado.
from functools import partial


class Foo:
    def __init__(self) -> None:
        self.public = 'isso é publico...'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privado'

    def metodo_publico(self):
        return 'metodo_publico'

    def _metodo_protected(self):
        return '_metodo_protected'

    def get_privado(self):
        return self.__private


f = Foo()
# print(f.public)
# print(f.metodo_publico())
# print(f._protected)
print(f.get_privado())
print(f._Foo__private)
