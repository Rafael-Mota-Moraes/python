"""
Cuidados com dados mutáveis
= - copiando o valor (imutáveis)
= - apontaa para o mesmo endereço na memória (mutável)
"""

nome = 'Rafael'
outra = nome
nome = 'Pedro'
print(nome)
print(outra)

lista_a = ['Rafa', 'Maria']
lista_b = lista_a

lista_a[0] = 'Qualquer coisa'
print(lista_b)
