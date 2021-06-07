from array import *
limit=int(input("Enter the Limit:"))
Number_list=array('I',[]) #here we are using array module because it stores only one type date which empowers us rather then []
for i in range(limit):
    number=int(input("Enter Elements : "))
    Number_list.append(number)
sum=0
for i in Number_list:
    sum+=i
    
print(f"The sum of {limit} elements you entered is ",sum)