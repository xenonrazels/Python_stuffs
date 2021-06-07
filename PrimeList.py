limit=int(input("Enter the limit :> "))
print(f"The prime number from 0 to {limit} are below")
prime_list=[]
for num in range(0,limit):
    if num > 1:
        for j in range(2,num):
            if num%j==0:
                break
        else:
            prime_list.append(num)
            print("Prime num:", num)
    

print("So, Prime list is ",prime_list)