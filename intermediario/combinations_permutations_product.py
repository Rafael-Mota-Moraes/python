# Combinations, permutations e product - Itertools


from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia'
]

camisetas = [
    ['preta', 'braca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino']
]


# print_iter(combinations(pessoas, 2))
# print()
# print_iter(permutations(pessoas, 2))
# print()
print_iter(product(*camisetas))
