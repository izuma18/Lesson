import os

list_paths = []

for adress, papka, file in os.walk('D:\\'):
    for i in file:
        full_path = os.path.join(adress, i)
        list_paths.append(full_path)

r = open('e.exe', 'rb')
y = open('Копия e.exe', 'wb')

while True:
    var = r.read(1048576)
    print(var.__sizeof__())
    if var.__sizeof__() == 33:
        break

    y.write(var)

print('Контроль')
r.close()
y.close()
