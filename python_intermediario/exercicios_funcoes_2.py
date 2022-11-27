# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multiplicar(numero, tipo):
    if tipo == 'duplicar':
        print(numero * 2)
    elif tipo == 'triplicar':
        print(numero * 3)
    elif tipo == 'quadruplicar':
        print(numero * 4)
    else:
        print('Digite uma operacao válida')

try:
    numero = input('Digite um número: ')
    numero_inteiro = int(numero)
    tipo = input('duplicar, triplicar ou quadruplicar? ')

    multiplicar(numero_inteiro, tipo)

except:
    print('Ocorreu um erro!')
