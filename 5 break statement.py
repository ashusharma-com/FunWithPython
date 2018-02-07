# 5. break statement
while True:
    str = input("Enter Your Name:")
    if len(str)>10 and str.__contains__(" "):
        print("Your name is:",str)
        break
    else:
        print("Please Enter Your Name like (FirstName LastName)")
