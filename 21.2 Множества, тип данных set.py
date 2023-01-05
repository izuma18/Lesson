z = {1, 2, 3, 4, 5}
x = {3, 4, 5, 6, 7}
v = {5, 6, 7, 8, 9}
z.add(6)  # Добавить
z.discard(1)  # Удалить
z.remove(2)  # Удалить при отсутствии будет ошибка
y = z.union(x)  # Объединить
v.update(z)  # Объединить
t = v.intersection(x)  # Объединить
e = v.difference(x)  # Показывает те значения которые не дублируются

print(z)
print(y)
print(v)
print(t)
print(e)
