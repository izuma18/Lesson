import os

h = [9, 8, 7, 4, 5, 6, 3, 2, 1, 5, 5]
'''
n = [x*2 for x in h] Генератор словарей
z = {x*2 for x in h} Генератор множеств
f = {x: x*2 for x in h} Генератор словарей
g = [x for x in h if x % 2 == 0 and x > 0]
'''

g = [os.path.join(z, i)
     for z, x, c in os.walk('D:\\')
     for i in c if '.txt' in i]
print(len(g))
