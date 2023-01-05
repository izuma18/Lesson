n = list(range(1, 21))
b = n.copy()  # Сохраняем копию потому что "списки" меняются
x = n[::]  # Синтаксис срезов [start:stop:step]
c = n[1::2]  # От какого индекса с каким шагом
s = n[5:7]  # От до
m = []

for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)

else:
    print(n)
    print(m)
    print(b)
    print(x)
    print(c)
    print(s)
