m=5
for i in range(m):
    for j in range(i+1):
        print((i+j)%m+1,end="")
    print("\n")