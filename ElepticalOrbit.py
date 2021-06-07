from vpython import *
from vpython.graph import *
scene=display(width=600,height=600,center=(0,5,0))
Sun=sphere(pos=(0,5,0),radius=100,color=color.orange)
earth=sphere(pos=(-200,0,0),radius=10,material=materials.earth,make_trial=true)
earthv=vector(0,0,5)
gd=gdisplay(x=800,y=0,width=600,height=600,foreground=color.black,background=color.white,xmax=3000,xmin=0,ymax=20,ymin=0)
f1=gcurve(color=color.blue)
t=0
for i in range(1000):
    rate(50)
    earth.pos=earth.pos+earthv
    dist=(earth.x**2 + earth.y**2 + earth.z**2)**0.5
    RadialVector=(earth.pos - Sun.pos)/dist
    Fgrav=-10000*RadialVector/dist **2
    earthv=earthv+Fgrav
    earth.pos+=earthv
    f1.plot(pos=(t,mag(earthv)))
    t+=1
    if dist<= Sun.radius:break
