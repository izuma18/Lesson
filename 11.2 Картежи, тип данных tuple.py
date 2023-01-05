x = (9, 8, 7, 6, 5, 4, 3)
y = []

# Изменение картежа в список
for i in range(len(x)):
    y.append(x[i] + 3)

print(x)
print(y)

# Изменение картежа в список и обратно
t = list(x)
t[0] = 10
x = tuple(t)
print(t)
