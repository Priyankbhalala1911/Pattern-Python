m=7
n=7

ap=65


for i in range(m):
    ap=65
    for j in range(i):
        print(" ",end="")
    for j in range(2*n,2*i,-1):
        # print(j)
        if(j>i+m):
            print(chr(ap),end="")
            ap=ap+1
        else:
            ap=ap-1
            print(chr(ap),end="")
    
            
    print("\n")