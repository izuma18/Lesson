def count_list(par):  # Параметр
    count = 0
    for i in par:
        count += 1
    return count


j = [9, 8, 7, 6]
print(count_list(j))  # Аргумент

h = ['a', 'a', 'h']
print(count_list(h))

k = [9, 8, 7, 5, 7, 5]
print(count_list(k))

print(count_list('stroka'))
