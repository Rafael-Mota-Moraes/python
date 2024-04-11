# Criando exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só precisa herdar alguma exceção da linguagem.
# A recomendação da documentação é herdar da Exception.
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11)

class MeuError(Exception):
    ...


class OutroError(Exception):
    ...


def levantar():
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note('Nota 1')
    exception_.add_note('Nota 2')
    exception_.add_note('Você errou tal coisa...')
    # 10 / 0
    raise exception_


try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    exception_ = OutroError('Lançando de novo...')
    exception_.__notes__ += error.__notes__.copy()

    raise exception_ from error
