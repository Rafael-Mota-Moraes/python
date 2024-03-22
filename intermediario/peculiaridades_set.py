# Sets são muito eficientes para remover valores duplicados de iteráveis
# Não possuem índices
l1 = [1, 1, 2, 2, 3, 3]
s1 = set(l1)
l2 = list(s1)
print(l2)
