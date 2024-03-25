import sys
iterable = ['Eu', 'teho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__


lista = [n for n in range(10000)]
generator = (n for n in range(10000))

print(sys.getsizeof(generator))  # muito mais leve
print(sys.getsizeof(lista))

print(next(generator))
print(next(generator))
print(next(generator))
