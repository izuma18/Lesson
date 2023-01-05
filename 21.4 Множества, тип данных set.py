r = open('text3.txt')
r1 = set(r.read().split())
r.close()

r = open('text4.txt')
r2 = (r.read().split())
r.close()

#new = r1.intersection(r2)
new = r1.difference(r2)

print(new)
