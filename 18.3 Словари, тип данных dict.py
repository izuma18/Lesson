d1 = {'a': 7}
d2 = dict()
d3 = dict.fromkeys([1, 2, 3, 4, 5], 'value')


if 'c' in d1:
    d1['c']

y = d1.get('c', 'value')
print(y)
