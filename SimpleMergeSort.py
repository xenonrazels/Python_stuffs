def mergeSort(a):
    print("Splitting",a)
    if len(a)>1:
        mid=len(a)//2
        LeftHalf=a[:mid]
        RightHalf=a[mid:]
        mergeSort(LeftHalf)
        print("Entered on right half")
        mergeSort(RightHalf)
        i=0
        j=0
        k=0
        while i<len(LeftHalf) and j<len(RightHalf):
            if LeftHalf[i]<RightHalf[j]:
                a[k]=LeftHalf[i]
                i+=1
                k+=1
            else:
                a[k]=RightHalf[j]
                j+=1
                k+=1
        while j< len(RightHalf):
                a[k]=RightHalf[j]
                j+=1
                k+=1
        while  i<len(LeftHalf):
                a[k]=LeftHalf[i]
                i=i+1
                k+=1
        print("Merging",a)
a=[323,546,23,5,4,7,34,768]
mergeSort(a)
print(a)
            