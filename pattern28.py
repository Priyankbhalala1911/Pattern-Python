m=5
a=1
for i in range(m):
    for j in range(m,i,-1):
        print("",end=" ")
    for j in range(i+1):
        print(a,end=" ")
        a+=1
    print("\n")