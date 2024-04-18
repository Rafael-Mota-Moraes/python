# os.listdir() para navegar em caminhos
# /home/pc-do-rafa/Área de Trabalho/faculdade
import os
caminho = os.path.join('/home', 'pc-do-rafa', 'Área de Trabalho', 'faculdade')

for pasta in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, pasta)
    if not os.path.isdir(caminho_completo):
        continue

    for arquivo in os.listdir(caminho_completo):
        print(arquivo)
