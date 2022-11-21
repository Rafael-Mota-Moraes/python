# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# Ae qualquer valor for considerado falso, a expressao inteira será avaliada naquele valor.
# São considerados falsy 0 0.0 '' False
# Também existe um tipo none que é usado para representar um não valor

entrada = input('[E]entrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123'
entrada_permitida = entrada == 'E' or entrada == 'e'

if entrada_permitida and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliações de curto circuito:
print(True or False)
print(False or True)
print(False or False)

# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

if senha != '123':
    print('Senha correta')
else:
    print('Senha incorreta')

print(not 0)
print(not not 0)

