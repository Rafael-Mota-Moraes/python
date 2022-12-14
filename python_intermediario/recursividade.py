def recursiva(inicio=0, fim=10):
    if inicio >= fim:
        return fim

    inicio += 1

    return recursiva(inicio, fim)


print(recursiva())
