m=5
n=5
ap=1
for i in range(m):
    
    if(i<1):
        for j in range(n,i,-1):
            print(" ",end="")
        for k in range(i+1):
            print(ap ,end="")
    else:
        for j in range(i+1):
            print(ap ,end="")
    ap+=1
    print("\n")