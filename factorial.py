def rec_fact(num):
    if num<0:
        print("\tSorry! \n\tYou dumb asshole have you ever seen factorial of negative numbers\n\tCorrect it bitch! ")
        return
    elif num==0:
        print("The factorial of 0 is 1")
        return
    if num==1:
        return num
    else:
        return num*rec_fact(num-1)
    
num=int(input("Enter a number :> "))
print("The factorial of",num,"is " ,rec_fact(num))
    