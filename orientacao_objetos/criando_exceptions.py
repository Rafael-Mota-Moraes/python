class MeuError(Exception):
    ...


class MeuOutroError(Exception):
    ...


def levantar():
    exception_ = MeuError('a', 'b', 'c')
    raise exception_


try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error)
    exception_ = MeuOutroError('Vou lançar de novo')
    raise exception_ from error