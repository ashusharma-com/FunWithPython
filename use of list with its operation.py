mycart = ['Mouse', 'Keybord', 'Laptop', 'DVD Writer']
print('I have', len(mycart), 'items to purchase.')
for item in mycart:
    print(item)
print('\nI also have to buy rice.')
mycart.append('Backpack')
print('My Cart list is now', mycart)
print('I will sort my list now')
mycart.sort()
print('Sorted Cart list is', mycart)
print('The first item I will buy is', mycart[0])
olditem = mycart[0]
del mycart[0]
print('I bought the', olditem)
print('My cart list is now', mycart)
