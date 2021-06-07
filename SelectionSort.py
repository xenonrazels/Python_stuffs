a=[5, 34, 90, 90, 98, 243]
def SelectionSort(a):
    for i in range(len(a)):
        least=i
        for k in range(i+1,len(a)):
            if a[k]<a[least]:
                least=k
            print(a)
        temp=a[least]
        a[least]=a[i]
        a[i]=temp
        # print(a)

print("The original list is",a)  
SelectionSort(a)
print(f"The final sorted list is:\n",a )
