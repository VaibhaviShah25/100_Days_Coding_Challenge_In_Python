# Day 81 of 100 days of coding challenge
# Program to make bouncing ball using turtle library
import turtle
import time
def moveleft():
    xb = ball.xcor()
    ball.setx(xb-10)
def moveright():
    xb = ball.xcor()
    ball.setx(xb+10)
def moveup():
    yb = ball.ycor()
    ball.sety(yb+10)
def movedown():
    yb = ball.ycor()
    ball.sety(yb-10)

win = turtle.Screen()
win.title("Bouncing ball")
win.bgcolor("cyan")

win.setup(width=600,height=600)
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.shapesize(stretch_wid=6, stretch_len=6)
ball.penup()

win.listen()

win.onkeypress(moveright,"r")
win.onkeypress(moveleft,"l")
win.onkeypress(moveup,"u")
win.onkeypress(movedown,"d")
h = 0
hy = 0
while True:
    if h == 0:
        moveright()
    if h == 1:
        moveleft()
    if ball.xcor() >= 300:
        h = 1
    if ball.xcor() <= -300:
        h = 0
    time.sleep(0.01)
    win.update()


win.winloop()

