# Operadores lógicos
# and (e)
# and - todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor.
# São considerados vaores falsos:
# 0 0.0 '' False
# Também existe o tipo None que é usado ara representar um não valor.

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input("Senha: ")
senha = '123'

if entrada == 'E' and senha_digitada == senha:
    print("Entrar")
else:
    print("Sair")
