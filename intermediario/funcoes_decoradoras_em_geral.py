# Funções decoradoras e decoradores
# Decorar = adicionar / remover / restringir / alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python usar as funções decoradoreas em outras funções

def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)

        resultado = func(*args, **kwargs)
        return resultado

    return interna


def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string')


inverte_string_checando_parametro = criar_funcao(inverte_string)

invertida = inverte_string_checando_parametro('Rafael')
print(invertida)
