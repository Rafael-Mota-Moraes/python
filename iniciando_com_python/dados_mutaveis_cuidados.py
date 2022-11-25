"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

# nome = 'Rafael'
# nome = 'João'
# print(nome)

# nome[1] = 'D'

lista_a = ['Luiz', 'Maria']
lista_b = lista_a
lista_c = lista_a.copy()

# lista_a[0] = 'Qualquer coisa'
lista_c[0] = 'Qualquer coisa'
print(lista_c)
