m=5
sum=1
for i in range(m):
    for j in range(m,i,-1):
        print(end=" ")
    for j in range(2*i+1):
        print(pow(sum,2),end=" ")
        sum+=1
    print("\n")