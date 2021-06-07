# Rember inorder to perform binary we alwyz need sorted data so
size=int(input("Enter  the size of list :> "))
List=[]
for i in range(size):
    num=int(input("Enter the number -> "))
    List.append(num)
Key=int(input("Enter the number you want to search in list => "))
List.sort()

def BinarySearch(List,Key,size):
    low=0
    high=size
    while low <= high:
        midpoint=int((low+high)/2)
        print(midpoint)
        if Key==List[midpoint]:
            return midpoint

        elif Key>List[midpoint]:
            low=midpoint+1
        else :
            high=midpoint-1
    return -1

if BinarySearch(List,Key,size) !=-1:
    print(f"The number {Key} is found at index={BinarySearch(List,Key,size)}.")
else:
    print(f'The number {Key} is not found.')
