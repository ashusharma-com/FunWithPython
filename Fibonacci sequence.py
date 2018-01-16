n1 = 0
n2 = 1
count = 0
limit = int(input("enter fibonacci sequence upto:"))
list = []
if limit <= 0:
   print("Please enter positive number")
elif limit == 1:
   print(n1)
else:
   print("Fibonacci sequence ",limit,":")
   while count < limit:
       list.append(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
print(list)