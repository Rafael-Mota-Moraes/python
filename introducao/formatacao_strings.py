"""
Formatação básica de strings
s - string
d - int
f - float
.<número de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(Quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'abc'
print(f'{variavel:a>10}')
print(f'{variavel:&<10}')
print(f'{variavel:|^10}')
print(f'{variavel:$^10}')
print(f'{1000.342891374589127809:-=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
