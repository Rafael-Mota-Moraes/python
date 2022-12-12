import copy
from dados import produtos

novos_produtos = [
    {**p, 'preco': p['preco'] * 1.1}
    for p in copy.deepcopy(produtos)
    
]
# print(*produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco'],
    reverse=True
)

print(*produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
