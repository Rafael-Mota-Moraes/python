# os.walk
# os.walk é uma função que permite percorrer uma estrutura de diretórios de maneira recursiva.
# Ela gera uma sequência de tuplas, onde cada tupla possui três elementos: o diretório atual (root), uma lista de subdiretórios (dirs), e uma lista dos aquivos do diretório atual (files).
import os
from itertools import count
caminho = os.path.join('/home', 'pc-do-rafa', 'Área de Trabalho', 'faculdade')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'pasta atual', files)

    for dir_ in dirs:
        print('    ', the_counter, 'Dir:', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        print('        ', the_counter, 'file:', caminho_completo_arquivo)
