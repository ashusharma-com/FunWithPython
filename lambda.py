
#sum of two values
ans = lambda val1, val2: val1+val2
print(ans(1,2))

#find the biggest value
big = lambda a, b: print("A is big", a) if a>b else print("B is big", b)
big(2,3)

#for loop with lambda
a = lambda x:[print(i) for i in x]
a(range(1,5))
