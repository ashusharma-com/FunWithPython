# 11. Local Variable
animal = "dog"
def func(animal):
    print("In funcation variable value: ", animal)
    animal="cat"
    print("after the variable value change: ", animal)

func(animal)
print("out of funcation value is still : ", animal)
