m=5
n=5


for i in range(m):
    for j in range(n,i,-1):
        print(" ",end="")
    for j in range(i+1):
        print(i-j+1,end=" ")
    print("\n")