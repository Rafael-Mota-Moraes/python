try:
    a = 18
    b = 1
    c = a / b
    print(c[10])
except ZeroDivisionError:
    print('tentou dividir por zero')
except NameError:
    print('Nome de variável não existe')
except (TypeError, IndexError) as error:
    print('MSG: ', error)
    print('Nome: ', error.__class__.__name__)
else:
    print('caiu no else')


print('continua...')
