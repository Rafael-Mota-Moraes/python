try:
    print('Abrir o arquivo...')
    8 / 0
except:
    print('Dividiu por zero...')
else:
    print('Não deu erro')
finally:
    print('Fechar arquivo...')
