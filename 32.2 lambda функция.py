list_of = [['Adam', 29], ['Jonne', 3 * 1 / 12], ['Jess', 25]]

r = sorted(list_of, key=lambda z: z[1])
print(r)

x = list(filter(lambda y: y[1] > 18, list_of))
print(x)
