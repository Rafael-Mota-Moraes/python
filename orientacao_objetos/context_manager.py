from contextlib import contextmanager

# class MyOpen:
#     def __init__(self, caminho_arquivo, modo):
#         self.caminho_arquivo = caminho_arquivo
#         self.modo = modo
#         self._arquivo = None

#     def __enter__(self):
#         self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf-8')
#         return self._arquivo
    
#     def __exit__(self, class_exeception, exception_, traceback_):
#         print('Exit')
#         self._arquivo.close()

#         # raise class_exeception(*exception_.args).with_traceback(traceback_)

#         # print(class_exeception)
#         # print(exception_)
#         # print(traceback_)

#         # return True

@contextmanager    
def my_open(caminho_arquivo, modo):
    print('Abrindo arquivo')

    arquivo = open(caminho_arquivo, modo, encoding='utf-8')
    yield arquivo
    print('fechando arquivo')
    arquivo.close()



instancia = my_open('context_manager.txt', 'w')

with instancia as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)
    pass
