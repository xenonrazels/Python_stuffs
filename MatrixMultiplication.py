a=[[2,5],[4,6]] 
b=[[3,5],[4,6]]
X=[[0,0],[0,0]]
for mat in range(X.__len__()):
    for row in range(a.__len__()):
        for col in range(a.__len__()):
            X[mat][row]=+a[mat][col]*b[col][row]
print(X)