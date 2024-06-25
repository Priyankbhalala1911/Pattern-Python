m=5
n=5


for i in range(m):
    sum=5
    for j in range(n):
        if(j<i):
            print(sum-i,end="")
            sum+=1
        else:
            print(m,end="")
            
    print("\n")