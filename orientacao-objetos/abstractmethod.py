from abc import ABC, abstractmethod


class AbstratFoo(ABC):
    def __init__(self, name) -> None:
        self._name = None
        self.name = name
        super().__init__()

    @property
    @abstractmethod
    def name(self): ...

    @name.setter
    @abstractmethod
    def name(self, name): ...


class Foo(AbstratFoo):
    def __init__(self, name) -> None:
        super().__init__(name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


foo = Foo('Bar')
print(foo.name)
