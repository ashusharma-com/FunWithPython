setA = set(['a', 'b', 'c'])
setB = set(['a', 'd', 'e'])
#intersection
a = setA & setB
print(a)
a = setA.intersection(setB)
print(a)
#union
a = setA | setB
print(a)
a = setA.union(setB)
print(a)
#a-b setA complement setB
a = setA - setB
print(a)


