import sys

url_list = ['text6.txt', 'text7.txt', 'text8.txt', 'text9.txt']

list_defect = []
list_info = []
save = []

try:
    for url in url_list:
        try:
            r = open(url)
            list_info.append(r.read())
            print('Здесь')

        except Exception:
            list_defect.append(url)
            print('Тут')
            sys.exit()  # Генерация ошибки
            continue
finally:
    r = open('save.txt', 'a')
    for i in list_info:
        r.write(i)
    r.write(str(list_defect))
    r.close()
    print('Я все записал')

print(list_info)
print(list_defect)

'''
Парсинг (parsing) — это сбор информации из сторонних источников и сайтов для использования полученных данных в различных 
целях, от аналитики до копирования, простыми словами, это сбор данных из различных источников.
'''
