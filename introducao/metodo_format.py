a = 'A'
b = 'B'
c = 1.1
string = 'a={b} b={a} c={numero:.2f}'
formato = string.format(a=a, b=b, numero=c)

print(formato)
