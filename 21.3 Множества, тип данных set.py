new = set()

r = open('text3.txt')
new.update(set(r.read().split()))
r.close()

r = open('text4.txt')
new.update(set(r.read().split()))
r.close()

print(new)
