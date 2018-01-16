import sys
data = []
print("\nTo stop type [exit]\n")
while True:
    x = input("Enter Value:")
    if x == "exit":
        print(data)
        sys.exit()
    else:
        data.append(x)
print(data)
