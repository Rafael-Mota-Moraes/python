"""
Introduçõ ao desempcotamento + tuples (tuplas)
"""

nomes = 'Maria', 'Helena', 'Luiz', 'João'
# nomes[1] = 'Outro'
nome1, *outros_nomes = nomes
print(nome1, outros_nomes)
print(type(nomes))
print(nomes)
