# 8. function
def say_hello():
	print("hello world")
say_hello()
		
# 9. function with arguments
def say_name(FirstName, LastName):
	print(FirstName, LastName)
say_hello("Anshuman", "Sharma")

# 10. function with return value
def get_sum(val0, val1):	
	return val0+val1
	
total = get_sum(33,22)
print(total)