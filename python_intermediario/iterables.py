iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__()  # Tem __iter__ e __next__

print(next(iterator))
print(next(iterator))
print(next(iterator))
