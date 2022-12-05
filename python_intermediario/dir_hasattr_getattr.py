string = 'Rafael'

# print(dir(string))

if hasattr(string, 'upper'):
    print('Existe upper')
    print(getattr(string, 'upper')())
    print(string.upper())
