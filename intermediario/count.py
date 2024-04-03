# count é um iterador sem fim (itertools)
from itertools import count

c1 = count(8, 8)
# print(next(c1))
# print(next(c1))
# print(next(c1))
# print(next(c1))

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))

# Loop infinito!
# for i in c1:
#     print(i)

print('count')
for i in c1:
    if i >= 100:
        break
    print(i)
