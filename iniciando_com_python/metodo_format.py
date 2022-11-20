a = 'A'
b = 'B'
c = 1.1

string = 'a={nome1} b={nome2} c={nome3:.2f} c_de_novo={nome3}'
formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)
