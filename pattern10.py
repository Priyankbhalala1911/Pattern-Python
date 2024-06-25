m=6
n=6


for i in range(m):
    for j in range(n,i,-1):
        print(end=" ")
    for j in range(2*i+1):
        print(abs(i),end="")
        i=i-1
    
    print("\n")