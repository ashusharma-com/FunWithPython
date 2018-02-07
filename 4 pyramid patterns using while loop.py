# 4. pyramid patterns using while loop	
i,j=0,0
while i != 5:
    while j < i+1:
        print("*",end=" ")
        j = j + 1
    print("\n")
    i = i + 1
    j=0
