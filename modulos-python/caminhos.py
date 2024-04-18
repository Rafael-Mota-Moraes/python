import os

caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
diretorio, arquivo = os.path.split(caminho)
nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
print(nome_arquivo, extensao_arquivo)
print(os.path.exists('C:\\Users\\rafael\\Desktop\\python\\modulos-python\\caminhos.py'))
print(os.path.exists(caminho))
print(os.path.abspath('.'))
print(os.path.basename(caminho))
