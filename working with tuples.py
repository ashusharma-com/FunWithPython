fruits = ('Apple', 'Apricot', 'Avocado')
print("Total Fruits: ", len(fruits))
new_fruits = fruits, 'Banana', 'Bilberry', 'Blueberry'
print('After adding other fruits the length : ', len(new_fruits))
print('All fruits : ', new_fruits)
print('3rd fruits is : ', new_fruits[0][2])
print('Last fruits is : ', new_fruits[3])
print('Total fruits', len(new_fruits)+len(new_fruits[0])-1)

#singltone tuple
m = ()
print(len(m))
m = ('1')
print(len(m))
m = ('1',)
print(len(m))
