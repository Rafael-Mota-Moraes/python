
s1 = set() # Vazio
# print(s1, type(s1))

s2 = {1,2,3,4} # Com dados
s3 = {3, 4, 3, 4, 1} # ELIMINAM NÚMEROS DUPLICADOS
print(s3)

print(3 in s3)

s3.add(9)
s3.add(('Rafael'))
print(s3)


s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
print(s3)
s3 = s1 & s2
print(s3)
s3 = s1 - s2
print(s3)

