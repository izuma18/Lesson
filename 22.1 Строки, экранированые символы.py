'''
s = 'Lets \
write a \
string as "s"'
'''

# Символ 'r' только для чтения
s = 'Let\'s write a string as "s"'

url = r'https:\\www.youtube.com\new'


print(s)
print(url)
'''
Экранированные последовательности, также называемые escape-последовательности, могут состоять из одного или 
нескольких символов после обратной косой черты:
\ в самом конце строки	Игнорируется, строка продолжается на новой строке
\\	Сам символ обратного слеша (остается один символ \)
\'	Апостроф (остается один ‘)
\"	Кавычка (остается один символ ")
\n	Новая строка (перевод строки)
\r	Возврат каретки
\t	Горизонтальная табуляция
\u…	16-битовый символ Юникода в 16-ричном представлении
\U…	32-битовый символ Юникода в 32-ричном представлении
\x…	16-ричное значение
\o…	8-ричное значение
\0	Символ Null (не признак конца строки)
'''