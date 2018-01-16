import sys
def binarySearch(data, item):
    try:
        first = 0
        last = len(data) - 1
        found = False
        while first <= last and not found:
            midpoint = (first + last) // 2
            if data[midpoint] == item:
                found = True
            else:
                if item < data[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
        if found is True:
            return "value found "
        else:
            return "value not found "
    except Exception as ex:
        print(ex)

data = []
print("\nTo stop type [exit]\n")
while True:
    x = input("Enter Value:")
    if x == "exit":
        print(data)
        find = input("Enter value to find:")
        print(binarySearch(data, int(find)))
        sys.exit()
    else:
        data.append(int(x))



