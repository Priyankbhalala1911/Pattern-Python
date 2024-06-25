m=5
for i in range(m):
    for j in range(2*i+1):
        if(j%2==0):
            print(i+1,end="")
        else:
            print("*",end="")
    print("\n")        

for i in range(m):
    for j in range(2*i+1,2*m):
        if(j%2!=0):
            print(m-i,end="")
        else:
            print("*",end="")
    print("\n")   