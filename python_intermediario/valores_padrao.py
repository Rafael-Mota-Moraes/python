def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} + {y=} + {z=}', x + y + z)
    else:
        print(f'{x=} + {y=}', x + y)


soma(1, 1)
soma(1, 4, 0)