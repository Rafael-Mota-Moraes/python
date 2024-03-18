"""
Iterável -> str, range, etc...
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o pŕ
"""

# for letra in texto
texto = 'Rafael'  # iterável
iterator = iter('Rafael')  # iterator


while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
