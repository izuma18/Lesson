x = [9, 8, 7, 6, 5]

# Добавляет элемент в конец списка
x.append(4)
print(x)

# Ставит объект перед индексом
x.insert(1, 7)
print(x)

# Показывает сколько одинаковых элементов в списке
print(x.count(7))

# Сортирует список по возрастанию
x.sort()
print(x)

# Переворачивает в обратную сторону
x.reverse()
print(x)

# Удалить и вернуть элемент по индексу (по умолчанию последним)
y = x.pop(0)
print(x)
print(y)

# Удалить первое вхождение значения
x.remove(7)
print(x)

# Удалить все элементы из списка
x.clear()
print(x)

# Расширьте список, добавив элементы из итерации
x.extend(['a', 's'])
print(x)

# Вернуть неглубокую копию списка
h = x.copy()
print(h)
