"""
split e join com list e str
split - divite uma string
join - une uma string
"""

frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split()
lista_frases = frase.split(',')
print(lista_palavras)

print(lista_frases)

for i, frase in enumerate(lista_frases):
    lista_frases[i] = lista_frases[i].strip()
    
print(lista_frases)
