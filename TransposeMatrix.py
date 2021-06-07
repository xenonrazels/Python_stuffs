a=[[3,4],[5,6],[8,8]]
T=[[0,0,0],[0,0,0]]
for i in range(a.__len__()):
    for j in range(a[0].__len__()):
        T[j][i]=a[i][j]
print(T)
            