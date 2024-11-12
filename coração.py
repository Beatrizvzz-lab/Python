import math
from turtle import*

def butterflya(r):
    return 15*math.sin(r)**3
def butterflyb(r):
    return 12*math.cos(r)-5*\
    math.cos(2*r)-2*\
    math.cos(3*r)-\
    math.cos(4*r)

speed(9000)
bgcolor("black")

for i in range(6000):
    goto(butterflya(i)*20,butterflyb(i)*20)
    for j in range(5):
         color("yellow")
         goto(0,0)
done()