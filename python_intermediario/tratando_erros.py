# a = 18
# b = 0

# try:
#     print('Linha 1')
#     c = a / b[0]
#     print('Linha 2')
# except ZeroDivisionError:
#     print('Dividiu por zero.')
# except NameError:
#     print('Variável não definida.')
# except (TypeError, IndexError) as error:
#     print('TypeError + IndexError')
#     print('MSG:', error)
#     print('Name:', error.__class__.__name__)
# except Exception:
#     print('Ocorreu algum erro na aplicação.')

# print('Depois do try')

try:
    print(1)
    # 8/0
except ZeroDivisionError:
    print('Dividiu por zero.')
else:
    print('Não deu erro')
finally:
    print(3)
