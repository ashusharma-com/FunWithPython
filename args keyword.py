def display(*args):
    total = 0
    for s in args:
        if type(s) is int:
            total = total + s
    print("total of all integers is:", total)


display("das", 2, 3, 4, 5, 6, 434, "123", "hello")
