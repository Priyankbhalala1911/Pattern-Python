m=7
for i in range(m):
    for j in range(m):
        print( m // 2 + 1 - min(min(i, j), min(m-1-i, m-1-j)) , end=" ")
    print("\n")