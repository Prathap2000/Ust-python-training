import math
#0.3048 is multipleto convert the feet into meter 
dis=int(input("enter the distance in feet :-"))*0.3048 
deg=int(input("enetr the angle:-"))
def hieght(dis,deg):
    rad=math.radians(deg)
    h= dis * (math.tan(rad))
    print("hieght in Meter",h)
hieght(dis,deg)