def dekor(f):
    def wrapper():
        try:
            h = f()
        except Exception:
            print('Повторите ввод...')
            h = f()
        return h
    return wrapper


@dekor  # make = decor(make)
def make():
    enter = float(input('Введите число: '))
    return enter


@dekor
def make2():
    enter = float(input('Введите число опять: '))
    return enter


make()
make2()
