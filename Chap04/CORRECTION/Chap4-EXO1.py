from turtle import *

def triangle(n):
    begin_fill()
    for _ in range(3):
        forward(n)
        left(120)
    end_fill()


up()
backward(100)
down()

for a in range(3):
    triangle(40)
    left(120)

up()
forward(100)
down()

for a in range(3):
    triangle(40)
    forward(80)
    left(120)



for a in range(40, 100, 20):
    up()
    goto(200-a,100-3*a)
    triangle(2*a)
    

