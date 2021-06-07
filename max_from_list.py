size=int(input("Enter  the size of list :> "))
List=[]
for i in range(size):
    num=int(input("Enter the number -> "))
    List.append(num)
max=List[0]
for i in range(size):
    if max <List[i]:
        max=List[i]
print(f"The max number in {List} is {max}")