a=[98, 90, 34, 5, 243, 56]
# a=[5, 34, 56, 90, 98, 243] #use it for tracing 
def insertion(a):
    for i in range(1,len(a)):
        current_value=a[i]
        position=i
        while position>0 and a[position-1]>current_value:
            a[position]=a[position-1]
            position=position-1
            # print(a) #use it for tracing see what differences between insertion sort and selection
        a[position]=current_value
        # print(a) # use it for tracing
print("Before sorting",a)
insertion(a)
print("After sorting",a)
            
            