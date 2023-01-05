x = (9, 9, 8, 7, 6, 5, 4, 3)
# Возвращает количество вхождений значения
print(x.count(9))

# Возвращает первый индекс значения.
# Вызывает ValueError, если значение отсутствует
print(x.index(7))

# Добавляем картеж в картеж
h = (1, 2, 3)
# Картеж не изменяемый тип данных получается 'g' новая переменная
g = h
h += (4, 5)
print(g)
print(h)
