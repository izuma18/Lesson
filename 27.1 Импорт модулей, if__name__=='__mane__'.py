#import newmod
import newmod as n  # Переименуем модуль для упрощенной работы
#from newmod import * Звездочка импортирует всё
from newmod import newf  # Импортируем нужную функцию

print(newf(3))
print(n.k)

'''
print(newmod.newf(3)) Работа функции из модуля
print(newmod.k) Импорт отдельной переменной
print(dir(newmod)) Показывает что есть в модуле
print(help()) Показывает что может модуль
'''