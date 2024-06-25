m=5
n=5
ap=1

for i in range(m):
    ap=1
    for j in range(n,i,-1):
        print(" ",end="")
    for j in range(2*i+1):
        print(ap,end="")
        ap=ap+1
    print("\n")