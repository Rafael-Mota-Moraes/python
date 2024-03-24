lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Rafael'}
]

for item in lista:
    if isinstance(item, set):
        item.add(10)
        print(item, isinstance(item, set))
