m=10
n=10

for i in range(m):
    for j in range(n,i,-1):
        print(end=" ")
    for j in range(i+1):
        print(end="*")
    print("\n")
    
for i in range(m):
    for j in range(i+2):
        print(end=" ")
        
    for j in range(n,i+1,-1):
        print(end="*")
    print("\n")