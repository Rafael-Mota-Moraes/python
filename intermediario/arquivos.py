import os

# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho_arquivo = './intermediario/arquivos.txt'

# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    print('Olá mundo...')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Atenção\n')

    print('Arquivo vai ser fechado...')

print()

with open(caminho_arquivo, 'r') as arquivo:
    print(type(arquivo))
    print(arquivo.read())

# os.unlink(caminho_arquivo)
os.rename(caminho_arquivo, 'arquivo.txt')
