m=10

for i in range(m):
    for j in range(i+1):
        if(i==j):
            print(0,end="")
        else:
            print(abs(i-m-j),end="")
    for j in range(i):
        print(m-j-1,end="")
        
    print("\n")
    