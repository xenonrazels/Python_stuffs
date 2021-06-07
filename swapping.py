num1=int(input("Enter the number1 :> "))
num2=int(input("Enter the number2 :> "))

def swap(a,b):
    temp=a 
    a=b 
    b=temp
    return a ,b
print("The number before swapping:",(num1,num2))
print("the number after swapping is :",swap(num1,num2))