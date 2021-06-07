num1=int(input("Enter your 1st number : "))
num2=int(input("Enter your 2nd number : "))
def gcd(num1,num2):
    
    remainder=num1%num2
    while remainder != 0:
        num1=num2
        num2=remainder
        remainder=num1%num2
    
    return num2
print(f"The GCD of {num1} and {num2} is {gcd(num1,num2)}")
    