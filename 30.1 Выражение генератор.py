h = ['https:\\www.сайт.com', 'https:\\www.какойтосайт.com',
     'https:\\www.левыйсайт.com', 'https:\\www.другойсайт.com',
     'https:\\www.сайтишка.com', 'https:\\www.сайтец.com', ]

n = [x.split('\\')[1] for x in h if '.com' in x]  # генератор списка
print(type(n))

z = (x.split('\\')[1] for x in h if '.com' in x)  # Выражение генератора
print(type(z))


'''
Выражение-генератор (generator expression) — выражение в круглых скобках которое выдает создает на каждой итерации
новый элемент по правилам. генератор коллекции — обобщенное название для генератора списка (list comprehension),
генератора словаря (dictionary comprehension) и генератора множества (set comprehension).
'''
