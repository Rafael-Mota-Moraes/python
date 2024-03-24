# Generator expression, iterables e terators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__

# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())

print(next(iterator))
print(next(iterator))
print(next(iterator))
