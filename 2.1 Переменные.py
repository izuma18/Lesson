number = 3
number = 4  # Переменная может ссылаться только на один объект памяти
number2 = 5
result = number + number2
print(result)

#Несколько переменных могут ссылаться на один и тот же объект
num1 = num2 = 5
print(num1, num2)

#Множественное присвоение
num_1, num_2 = 5, 7
print(num_1, num_2)

#Обмен значений в переменных
swap1 = 8
swap2 = 9
swap1, swap2 = swap2, swap1
print(swap1, swap2)

#Так же можно провести математическую операцию
swap1 = 8
swap2 = 9
swap1, swap2 = swap2, swap1 + swap2
print(swap1, swap2)

#Уменьшение с разными объектами
swap2 = swap2 - number
#Так же можно написать +-*/=
#swap2 -= number
print(swap2)
