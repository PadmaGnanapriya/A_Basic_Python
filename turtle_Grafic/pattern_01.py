import turtle
girish = turtle.Turtle()
girish.speed('fastest')
for i in range (100):
    girish.forward(100)
    girish.pencolor("black")
    girish.right(90)
    girish.forward(100)
    girish.left(90)
    girish.forward(100)
    girish.right(90)
    girish.penup()
    girish.setposition(0, 0)
    girish.pendown()
    girish.pencolor("blue")
    girish.right(2)
turtle.done()