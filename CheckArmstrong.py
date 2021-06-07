#Armstrong are the digit which is equal to sum of Cubes of its each digit i.e 153=(1*1*1)+(5*5*5)+(3*3*3)=153
def checkArmstrong(digits):
    temp=digits
    sum=0
    while temp > 0:
        n=temp%10
        sum+=n**3
        temp=temp//10
    if sum==digits:
        return True
    else:
        return False
num=int(input("Enter the number that you want to check Armstrong :>"))

if  checkArmstrong(num):
    print(f"The Given number {num} is armstrong")
else:
    print("The Given number is not armstrong")
        
        
    