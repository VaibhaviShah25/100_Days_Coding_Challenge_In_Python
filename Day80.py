# Day 80 of 100 days of coding challenge
# Draw circles using Turtle Library
import turtle
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(20)
c = ["#00bfff","#4682b4","#0000cd","#00008b","#191970"]
k = 0
for i in range(4):
    k = 4
    for i in range(100,0,-20):
        t.color(c[k])
        k -= 1
        t.begin_fill()
        t.circle(i)
        t.end_fill()
    t.right(90)
t.end_fill()
turtle.done()

