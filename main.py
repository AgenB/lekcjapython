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

def chess(x, y, l, c1, c2):
    for i in range(y):
        for j in range(x):
            if ((i + j) % 2 == 0):
                poly(4, l/x, c1)
            else:
                poly(4, l/x, c2)
            t.forward(l/x)
        t.pu()
        t.backward(l)
        t.right(90)
        t.forward(l/x)
        t.left(90)
        t.pd()

def tree(n, a):
    if n == 0: return
    t.fd(a); t.lt(30)
    tree(n-1, a/2)
    t.rt(60)
    tree(n-1, a/2)
    t.lt(30); t.bk(a)

def drawTree(degree):
    t.pu(); t.home(); t.seth(90); t.bk(240); t.pd()
    tree(degree, 240)

drawTree(7)

#chess(8, 8, 120, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (random.randint(0,255),random.randint(0,255),random.randint(0,255)))

input()