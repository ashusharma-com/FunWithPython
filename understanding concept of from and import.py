# understanding concept of from and import

mydata.py
------------------
text= "Welcome"

def add(a, b):
   print((a+b))

def sum(a, b):
   print((a-b))

def mul(a, b):
   print((a*b))

demo.py
-----------------
from mydata import add, mul, sum, text

add(1,2)
sum(5,2)
mul(2,1)
print(text)


