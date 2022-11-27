
def saudacao(msg, nome):
    return f'{msg}, {nome}'


def executa(func, *args):
    return func(*args)


v = executa(saudacao, 'Olá', 'João')

print(v)