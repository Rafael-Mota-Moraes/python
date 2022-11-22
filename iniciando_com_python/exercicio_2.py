"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_digitado = input('Digite um número INTEIRO: ')

numero_e_par = None

try:
    numero_inteiro = int(numero_digitado)
    numero_e_par = numero_inteiro % 2 == 0
except:
    print('Digite um número válido!')

if numero_e_par:
    print('Número é par.')
else:
    print('Número é impar')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_atual = input('Digite sua hora atual (sem minutos ou segundos):')

try:
    hora_atual = int(hora_atual)
    
    if hora_atual >= 0 and hora_atual <= 11:
        print('Bom Dia')
    elif hora_atual >= 12 and hora_atual <= 17:
        print('Boa tarde')
    elif hora_atual >= 18 and hora_atual <= 23:
        print('Boa noite')
    else:
        print('Digite um horário válido!')
except:
    print('Digite um número inteiro!')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome_usuario = input('Digite seu nome: ')
tamanho_nome = len(nome_usuario)

if tamanho_nome <= 4:
    print('Seu nome é curto')
elif tamanho_nome >= 5 and tamanho_nome <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
