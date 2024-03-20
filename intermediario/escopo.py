"""
Escopo de funçoes em Python
Escopo significa o local onde aquele código pode atingir
Existe escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
"""

y = 1
x = 10


def escopo():
    global x
    x = 1
    print(f'{x=}')
    print(f'{y=}')

    def outra_funcao():
        z = 1
        print(f'{x=}')
        print(f'{z=}')

    outra_funcao()

# print(x) # variável x só existe dentro da função


print(x)
escopo()
print(x)
