import sys

data = sys.argv
total = 0
if len(sys.argv) > 3:
	if(data[1]=="-add"):
		for i in data[2:]:
			total = total + int(i)
		print("Addition is = ", total)
	elif(data[1]=="-sub"):
		for next in data[2:]:
			if total is not 0:
				total = total - int(next)
			else:
				total = int(next)
		print("Subtraction is = ", total)
	elif(data[1]=="-mul"):
		total = 1
		for i in data[2:]:
			total = total * int(i)
		print("Multiplication is = ", total)
	elif(data[1]=="-div"):
		for next in data[2:]:
			if total is not 0:
				total = total / int(next)
			else:
				total = int(next)
		print("Division is = ", total)
	else:
		print("\nPlease Enter Details Like\n ..>python ", sys.argv[0], " [-add/-sub/-mul/-dev] num1 num2 numN..")
else:
    print("\nPlease Enter Details Like\n ..>python ", sys.argv[0], " [-add/-sub/-mul/-dev] num1 num2 numN..")
