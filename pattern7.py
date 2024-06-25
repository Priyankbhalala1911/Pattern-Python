m=5
n=5

count = 4

for i in range(m):
    for j in range(count):
        print(end=" ")
        
    for j in range(n-count):
        print(end="* ")
    count-=1
    print("\n")
    

    
        