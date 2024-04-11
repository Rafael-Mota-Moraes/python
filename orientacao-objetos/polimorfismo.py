# Polimorfismo é o prinipio que permite que classes derivadas dde uma mesma superclasse tenham métodos iguais (com mesma assinatura) mas comportamentos diferentes.
# Assinatura do método = mesmo nome e quantidade de parâmetros (retorno não faz parte da assinatura)
# AAssinatura do método: nome, parâmetros e retorno iguais
# SO "L" ID
# principio da substituição de Liskov
# Objetos de uma superclasse devem ser substituíveis por objetos de uma subclasse sem quebrar a aplicação
from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:
        ...


class NotificacaoEmail(Notificacao):
    def enviar(self):
        print('Email: enviando...')
        print(self.mensagem)
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando...')
        print(self.mensagem)
        return True


def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação não enviada')


notificar(NotificacaoEmail('Testando...'))
notificar(NotificacaoSMS('Testando...'))
