import math
x1=int(input("Enter the x1 :> "))
x2=int(input("Enter the x2 :> "))
y1=int(input("Enter the y1 :> "))
y2=int(input("Enter the y2 :> "))

def distance(x1,y1,x2,y2):
    dist=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return dist


print(f"The distance between the point {x1,x2} and {y1,y2} is {distance(x1,y1,x2,y2)}")

    
