# Introdução às Generator functions
# generator = (n for n in range(100))

def generator(n=0, maximum=10):
    for i in range(n, maximum):
        yield i


gen = generator(n=0)
print(next(gen))
print(next(gen))
print(next(gen))
