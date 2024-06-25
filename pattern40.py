m=5

for i in range(m):
    a=65
    for j in range(m,i,-1):
        print(chr(a+i),end="")
        a+=1
    print("\n")