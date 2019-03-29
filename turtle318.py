import turtle

kaz = turtle.Turtle()

kaz.color("blue", "cyan")
#   (#3cc9118) Hex Value or RGB Value

kaz.pensize(1)

kaz.shape('turtle')

# kaz.forward(100)
# kaz.left(90)
# kaz.penup()
# kaz.forward(100)
# kaz.right(90)
# kaz.pendown()
#
# kaz.forward(100)

kaz.begin_fill()


kaz.forward(100)
kaz.left(90)
kaz.forward(100)
kaz.left(90)
kaz.forward(100)
kaz.left(90)
kaz.forward(100)

kaz.penup()
kaz.forward(150)
kaz.pendown()

kaz.forward(100)
kaz.left(90)
kaz.forward(100)
kaz.left(90)
kaz.forward(100)
kaz.left(90)
kaz.forward(100)






kaz.end_fill()

turtle.done()