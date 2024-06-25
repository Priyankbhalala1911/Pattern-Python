m=5

for i in range(m):
    for j in range(i+1):
            print(i-j+1,end="")
    for j in range(i):
        print(j+2,end="")
    print("\n")