# Декораторы — это, по сути, "обёртки", которые дают нам возможность изменить поведение функции, не изменяя её код.
def dekor(f):
    def wrapper():
        print('Код декоратора')
        f()
        print("Второй код декоратора")
    return wrapper


@dekor  # make = decor(make)
def make():
    enter = input('Enter something... ')
    print(enter)


print('Здесь')
make()
