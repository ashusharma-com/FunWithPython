try:
    f = open("tmp.txt","r")
except IOError as err:
    print(err)
    try:
        total = 2/0
    except Exception as err:
        print(err)