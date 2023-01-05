'''
r = open('file.txt', 'a')
r.write('something' + '\n')
r.write('Что-то')
r.close()

print('Все норм')
'''

# with закрывает файл безопасно

with open('file.txt', 'a') as r:
    r.write('something' + '\n')
    10/0
    r.write('Что-то')

print('Все норм')
