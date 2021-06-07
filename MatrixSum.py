# programn to add two matrices
#  |   
#  |
#  |

a=[[2,5,5],[4,6,3],[2,5,6]] 
b=[[3,5,6],[4,6,5],[6,2,8]]
X=[[0,0,0],[0,0,0],[0,0,0]]
for row in range(a.__len__()): #a.__len__ represents rows
    for col in range(a[0].__len__()): #a[0].__len__ can represents columns
        X[row][col]= a[row][col]+b[row][col]
print(X) 
