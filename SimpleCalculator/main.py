from operations import * 

def main():
    print("Our Simple Calculator Menu:")
    print("\t\1. Addition \n\t2. Substraction \n\t3. Mulplication \n\t4. Division \n\t5. Integer Division \n\t6. Power")
    choice=int(input("Enter the operation you want to perform(/1/2/3/4/5/6):"))
    number1=int(input("Enter the first number :> "))
    number2=int(input("Enter the second number :> "))
    
    if choice==1:
        print(f"{number1} + {number2} = {add(number1,number2)}")
    elif choice==2:
        print(f"{number1}-{number2} = {sub(number1,number2)}")
    elif choice==3:
        print(f"{number1}*{number2} = {multiply(number1,number2)}")
    elif choice==4:
        print(f"{number1} / {number2} = {divide(number1,number2)}")
    elif choice ==5:
        print(f"{number1}//{number2} = {intergerDiv(number1,number2)}")        
    elif choice ==6:
        print(f"{number1} ^ {number2} = {sub(number1,number2)}")
    else:
        print("Your choice is wrong. ")

if __name__=='__main__':
    main()