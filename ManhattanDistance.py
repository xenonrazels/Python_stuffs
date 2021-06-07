import math 
x1=int(input("Enter the x1 :> "))
x2=int(input("Enter the x2 :> "))
y1=int(input("Enter the y1 :> "))
y2=int(input("Enter the y2 :> "))
def distance(x1,x2,y1,y2):
    dist=math.fabs(x2-x1)+math.fabs(y2-y1)
    return dist

print("The Manhattan distance between points {x1,y1} and {x2,y2} is",distance(x1,y1,x2,y2))