import math
x,y,vx,vy=int(input()),int(input()),int(input()),int(input())
if(x<=0 or y<=0 or vx<=0 or vy<=0):
    print("Invalid Input")
else:
    min=math.sqrt(x*x+y*y)
    while(x>=0 or y>=0):
        x-=vx
        y-=vy
        d=math.sqrt(x*x+y*y)
        if(d<min):
            min=d
    if(min==0.0):
        print("0.0")
    else:
        print("{0:.11f}".format(min))
