def multiplication(num,limit):
    print(f"\n\t\tMultiplication table for {num} is below:")
    for i in range(1,limit+1):
        print(f"{num} * {i} = {num*i}")

num=int(input("Enter the number for which You want multiplication table :> "))
limit=int(input("Enter the limit :> "))
multiplication(num,limit)

        
        
        