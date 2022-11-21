"""
Formatação básica de strings
s - string
d - int
f - float
.<numero de digitos>f
x ou X - Hexadecimal
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>100,.1f
Conversion flags - !r !s !a
"""

variavel = 'abc'
print(f'{variavel}')
print(f'{variavel:?>10}')
print(f'{variavel:-<10}.')
print(f'{variavel:=^10}.')
print(f'{1000.38748239049239:+,.1f}')
