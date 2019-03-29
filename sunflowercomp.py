import turtle
import math

sal = turtle.Turtle()

sal.color("red", "yellow")
sal.speed(10)

sal.begin_fill()

for i in range(2000):
    sal.forward(10)
    sal.left(math.sin(i/10)*25)
    sal.left(20)


#sal.end_fill()

turtle.done()







turtle.done()

