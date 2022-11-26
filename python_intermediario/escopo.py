x = 1000
def escopo():
    x = 10

    def outra_funcao():
        y = 2
        print(x, y)
    # x = 1
    outra_funcao()
    print(x)

# print(x)
x = 1
escopo()
 