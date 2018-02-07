# 12. global statement
animal = "dog"
def func():
    global animal
	#global animal,vehicle,....
    print("In funcation variable value: ", animal)
    animal="cat"
    print("after the variable value change: ", animal)

func()
print("out of funcation, value is changed: ", animal)