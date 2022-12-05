def generator(n=0, maximun=10):
    while True:
        yield n
        n += 1
        
        if n > maximun:
            return 'terminou'



gen = generator()
# print(gen.__iter__())
# print(next(gen))
# print(next(gen))

for n in gen:
    print(n)
