"""
Introdução às funções (def) em python
Funções são trechos de código usados para replicar uma determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.
Por padrão, funções Python retornam None (nada)
"""


def imprimir(msg, end='\n'):
    print(msg, end=end)


def saudacao(nome):
    print(f'Olá, {nome}')


imprimir("Olá mundo")
saudacao('Rafa')
