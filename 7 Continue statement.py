# 7. Continue statement
while True:
    str = input("Enter Your Name with length 10 to 15 :")
    if len(str)>10 and str.__contains__(" "):
        print("Your name is:",str)
        if len(str) >10 and len(str) < 15 :
            continue
        else:
            break
    else:
        print("Please Enter Your Name like (FirstName LastName)")
