# Operadores in e not in
# Strings são iteraveis!

# 0 1 2 3 4 5
# R a f a e l

# nome = 'Rafael'
# print(nome[2])

# print('a' in nome)
# print('a' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
