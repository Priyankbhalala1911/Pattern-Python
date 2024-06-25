m=5
n=5

for i in range(m):
    for j in range(i+1):
        if(j%2==0):
            print(1,end="")
        else:
            print(0,end="")
    print("\n")