m=5
for i in range(m):
    for j in range(m,i,-1):
        if(i%2==0):
            print(1,end="")
        else:
            print(0,end="")
    print("\n   ")