"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321

Fatiamento [i:f:p] [::]
Obs.: A função len retorna a qtd de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[-4])
print(variavel[4:8:1])
print(len(variavel))
print(variavel[0:len(variavel):2])
