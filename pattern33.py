m=5
for i in range(m):
    for j in range(m):
        if(j==0 or j==(m-1) or i==0 or i==(m-1)):
            print(1,end=" ")
        else:
            print(" ",end=" ")
    print("\n")