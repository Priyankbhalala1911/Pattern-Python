m=5

for i in range(m):
    for j in range(i+1):
        print(j+1,end="")
        
    for j in range(2*m,2*i+2    ,-1):
        print(" ",end="")
      
    for j in range(i+1):
        print(i-j+1,end="")
    print("\n")