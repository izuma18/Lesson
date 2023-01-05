price = {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}

new_price = {}
for i in price:
    #print(i)
    new_price[i] = round(price[i] * 0.85, 2)


print(price)
print(new_price)
