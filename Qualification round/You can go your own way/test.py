
from turtle import *
import sys

P1 = sys.argv[1]
P2 = sys.argv[2]

D = 40

speed(0)

color("blue")
for p in P1:
    if p == 'S':
        setheading(270)
    else:
        setheading(0)
    
    forward(D)
    
up()
home()
down()

color("red")
for p in P2:
    if p == 'S':
        setheading(270)
    else:
        setheading(0)
    
    forward(D)
    
input()
