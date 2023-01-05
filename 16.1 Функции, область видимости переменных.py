x = 5
count = 0
while count < 3:
    count += 1
print(count)
# это все видимое


def name():
    y = 10
    print(x)


name()
print(y)  # NameError: name 'y' is not defined
# это не видимое значение
