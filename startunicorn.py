import turtle

startunicorn = turtle.Turtle()
startunicorn.getscreen().bgcolor("#FF5234")

startunicorn.penup()
startunicorn.goto((-200, 100))
startunicorn.pendown()

def star(turtle, size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            startunicorn.forward(size)
            star(turtle, size/3)
            startunicorn.left(216)
        turtle.end_fill()



star(startunicorn, 360)


turtle.done()