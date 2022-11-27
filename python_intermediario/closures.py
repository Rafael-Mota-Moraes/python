def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'

    return saudar
        

saudacao_1 = criar_saudacao('Bom dia', 'Pedro')
print(saudacao_1)
print(saudacao_1())
