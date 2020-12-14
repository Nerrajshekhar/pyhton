x = int(input("enter the number of lines u want to print"))
for i in range(x):
    for j in range(x - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", sep="", end="")
    for l in range(x - 1 - i):
        print(" ", end="")
    print()
for i in range(x-1,0,-1):
        for j in range(x - i):
            print(" ", end="")
        for k in range(2 * i - 1):
            print("*", sep="", end="")
        for l in range(x - i):
            print(" ", end="")
        print()
