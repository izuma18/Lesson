price = {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}

new_price = {}
for i in price:
    new_price[i] = round(price[i] * 0.85, 2)
print(new_price)


new_price = {}
new_d = {i: round(price[i]*0.85, 2) for i in price.keys()}
print(new_d)
