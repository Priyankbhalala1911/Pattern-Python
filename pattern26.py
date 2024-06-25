m=5
sum=1
for i in range(m):
    for j in range(i+1):
        print(sum+j,end="")
    for j in range(i):
        print(sum+j,end="")
    sum+=1
    print("\n")