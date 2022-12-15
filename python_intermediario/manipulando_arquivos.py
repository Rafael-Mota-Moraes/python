import os

caminho_arquivo = 'C:\\Users\\Rafael\\Desktop\\python\\python_intermediario\\'
caminho_arquivo += 'manipurando_arquivos.txt'

# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0, 0)
#     # print(arquivo.read())
#     arquivo.seek(0, 0)

#     for linha in arquivo.readlines():
#         print('for:', linha, end='')

#     print('Arquivo foi fechado...')

# print('#' * 30)

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())
#     print('Arquivo foi fechado...')

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n', 'Atenção')
    )

deletar = input('Deseja deletar o arquivo? [S]im [N]ão. ')

if deletar == 'S':
    os.remove(caminho_arquivo)
