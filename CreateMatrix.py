# write a program to ask the dimension of matrix i.e row*column 
#Then create the matrix and print it like as of matrix form 
col=int(input("Enter the number of columns :> "))
row=int(input("Enter the number of rows :> "))
Matrix=[]*0

print("Let Matrix element is represented as A(ij):")
for ro in range(row):
    a=[]                                                            # for rows: It will be called: as the  number of rows You need
    for co in range(col):
        a.append(int(input(f"Enter the elements for a{ro}{co} :> "))) #acts as col with element
    Matrix.append(a)
print(f"\n Your matrix of dimension {row}*{col} is:{Matrix} i.e")        
for i in Matrix:
    print("      ", i)
