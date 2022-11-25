salas = [
    ['João', 'Maria'],
    ['Marcela', 'Joana'],
    ['Alberto', 'Antonio']
]

for sala in salas:
    for nome in sala:
        print(f'Sala {salas.index(sala)}) {nome}')