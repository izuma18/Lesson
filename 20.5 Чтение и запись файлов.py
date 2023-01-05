r = open('text2.txt', 'w', encoding='utf-8')
r.write('stroka текста')

r.close()


h = open('text2.txt', encoding='utf-8')
print(h.read())