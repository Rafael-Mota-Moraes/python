primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite um valor: ')

if primeiro_valor > segundo_valor:
    print(f'Primeiro valor {primeiro_valor=} é maior.')
elif primeiro_valor < segundo_valor:
    print(f'Segundo {segundo_valor=} valor é maior.')
else: 
    print('Valores iguais ou inválidos.')
