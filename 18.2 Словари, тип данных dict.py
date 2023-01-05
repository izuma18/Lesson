d1 = {'a': 7}
d2 = dict()
d3 = dict.fromkeys([1, 2, 3, 4, 5], 'value')

d5 = d1.copy()
print(d1.items())
print(d1.keys())
print(d1.values())
print(d1.update(d2))

t = d1.pop('a')
print(t, d1)
