m=5
for i in range(m):
    for j in range(2*i+1):
        print(j+1,end="")
    print("\n")
for i in range(m-1):
    for j in range(2*m,2*(i+1)+1,-1):
        print(2*m-j+1,end="")
    
    print("\n")
