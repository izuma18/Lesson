def show():
    print('Функция')


def show2():
    x = 7
    return x


y = show2()
print(y)

z = show2() + 9
print(z)

print(show())
# print(x) NameError: name 'x' is not defined, значение не найдено
