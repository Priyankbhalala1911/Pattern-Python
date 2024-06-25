m=5
n=5

for j in range(m):
    for i in range(1,n-j+1):
        print(i,end="")
        
    for i in range(2*(j)):
        print("*",end="")
        
    for i in range(n-j,0,-1):
        print(i,end="")
    print("\n")