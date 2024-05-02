import random

r_range = random.randrange(10, 20, 2)
print(r_range)
print(random.randint(1, 10))
nomes = ['Ana', 'Bernardo', 'Clécio', 'Eduardo']
random.shuffle(nomes)
print(nomes)

novos_nomes = random.sample(nomes, k=2)
print(novos_nomes)
