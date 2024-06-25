m=5
sum=1
for i in range(m):
    for j in range(m,i,-1):
        print(sum,end=" ")
        sum+=1
    print("\n")