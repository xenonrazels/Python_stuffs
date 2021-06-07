size=int(input("Enter  the size of list :> "))
List=[]
for i in range(size):
    num=int(input("Enter the number -> "))
    List.append(num)
search_number=int(input("Enter the number you want to search in list => "))
for i in range(size):
    if search_number == List[i]:
        print(f'Number {search_number} is found at {i} index in list=>{List}')
        break

print("Sorry! Number is not found")

