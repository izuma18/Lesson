s = 'stroka texta'

print(s[0:5])
print('strok' in s)

print(s.upper())  # Большие буквы
print(s.lower())  # Маленькие буквы
print(s.capitalize())  # Первая буква большая

# Меняем слеш с linux
path = 'D:/Lesson'
path1 = path.replace('/', '\\')  # D:\Lesson
print(path1)

# Получение отдельной строки имени файла
r = path1.split('\\')
print(r[-1])
