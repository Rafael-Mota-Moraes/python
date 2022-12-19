class Foo:
    def __init__(self):
        self.public = 'Isso é publico!'
        self._protected = 'Isso é protegido!'
        self.__exemplo = 'Isso é private'

    def metodo_publico(self):
        print(self.__exemplo)
        return 'metodo_publico'

    def _metodo_protected(self):
        return '_metodo_protected'

    def __metodo_private(self):
        return '_metodo_private'


f = Foo()
f.metodo_publico()
