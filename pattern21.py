m=5
n=5

for i in range(m):
    for j in range(n,i+1,-1):
        print(j,end="")
    for j in range(i+1):
        
        if(j==0):            
            print("*",end="")
        else:
            print(i-j+1,end="")
 
    print("\n")
        