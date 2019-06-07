import turtle
import random

t = turtle.Turtle()
turtle.colormode(255)
t.speed(100)

def poly(n, d, color):
    t.begin_fill()
    t.color(color)
    for i in range(n):
        t.forward(d)
        t.left(360/n)
    t.end_fill()

color1 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
color2 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

for i in range(8):
    for j in range(8):
        if ()
        poly(4, 10, color1)
        t.forward(10)
    t.pu()
    t.backward(80)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.pd()

input()