def some():
    with open('text9.txt', encoding='utf-8') as r:
        for x in r:
            yield x


p = some()

for i in p:
    print(i)

'''
print(next(p))  # Первая функция next
print(next(p))  # Вторая функция next
print(next(p))  # Третья функция next
'''
