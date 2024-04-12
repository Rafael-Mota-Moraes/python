# Context Manager com classes
# Você pode implementar seus próprios protocolos apenas imlementando os dunder methods que o Python vai usar.
# Isso é chamado de Duck typing. Um conceito relacionado com tipagem dinâmica onde o Python não está interessado no tió, mas se alguns métodos existem no seu objeto para que ele funcione de forma adequada.
# Para criar um context manager, os métodos __enter__ e __exit__ devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o treceback. Se ele retornar True, exceção no with sera suprimida.

class MyOpen:
    def __init__(self, caminho_arquivo, modo, encoding):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self.encoding = encoding
        self._arquivo = None
        print('init')

    def __enter__(self):
        print('Abrindo arquivo...')
        self._arquivo = open(self.caminho_arquivo,
                             self.modo, encoding=self.encoding)
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('Fechando arquivo...')
        self._arquivo.close()

        exception_.add_note('Minha nota')

        raise class_exception(*exception_.args).with_traceback(traceback_)


with MyOpen('./arquivo.txt', 'w', 'utf8') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3', 123)
    print('WITH', arquivo)
