'''
def some():
    list_text = []
    with open('text9.txt', encoding='utf-8') as r:
        for x in r:
            list_text.append(x)
    return list_text
'''

def some():
    with open('text9.txt', encoding='utf-8') as r:
        for x in r:
            yield x


for i in some():
    print(i.split())


'''
Yield — это ключевое слово в Python, которое используется для возврата из функции с сохранением состояния ее локальных 
переменных, и при повторном вызове такой функции выполнение продолжается с оператора yield, на котором ее работа была 
прервана.
'''


