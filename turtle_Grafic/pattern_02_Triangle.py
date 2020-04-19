import turtle

Padme=turtle.Turtle()
turtle.bgcolor("black")
turtle.pensize(4)          #Sharpness & thikness of the printed lines
turtle.speed(10)
b=["red","yellow","lightgreen","white"]


for i in range (15):
    for a in b:
        Padme.color(a)
        Padme.forward(i*10)
        Padme.right(120)

for i in range (15):
        Padme.color(a)
        Padme.forward(i*5**2)
        Padme.right(120)


turtle.done()