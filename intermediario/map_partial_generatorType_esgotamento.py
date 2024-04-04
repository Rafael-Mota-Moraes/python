# map - para mapear dados
from functools import partial
from types import GeneratorType


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def muda_preco_de_produtos(produto):
    return {**produto, 'preco': round(produto['preco'] * 1.1, 2)}


novos_produtos = map(
    muda_preco_de_produtos,
    produtos
)

print_iter(novos_produtos)
print(novos_produtos)  # tem __iter__ e __next__
print(isinstance(novos_produtos, GeneratorType))

print()

print(
    list(
        map(
            lambda x: x * 3,
            [1, 2, 3, 4]
        )
    )
)
