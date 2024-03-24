string = 'Rafael'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe o método upper')
    # string = string.upper()
    print(getattr(string, metodo)())
else:
    print('Não existe o método upper')

print(string)
