def saudacao(nome):
    return f'Olá, {nome}'


def executa(funcao, texto):
    return funcao(texto)


v = saudacao('Rafael')
print(v)

v1 = executa(saudacao, 'Rafael')
