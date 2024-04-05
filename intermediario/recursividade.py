# Funções recursivas e recursividade
# - Funões que podem se chamar de volta
# - Úteis p/ dividir provlemas grandes em partes menores
# Toda Função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial de n = n! = n-1 * n-2...n-n+1

def recursiva(inicio=0, fim=10):
    # caso base
    if inicio >= fim:
        return fim

    # Caso recursivo
    # Contar até chegar ao final
    print(inicio, fim)
    inicio += 1
    return recursiva(inicio, fim)


def fatorial(num):
    if num <= 1:
        return 1

    return num * fatorial(num - 1)


print(recursiva())
print("Fatorial:", fatorial(5))
