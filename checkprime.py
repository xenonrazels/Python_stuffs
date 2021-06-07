num=int(input("Enter the number to check prime: "))
if num ==0 or num==1:
    print("The number is not prime")
for i in range(2,num):
    if num % i  == 0:
        r=num/i
        print("Sorry! not prime")
        break
else:
    print(f"Yes! number {num} is prime")

