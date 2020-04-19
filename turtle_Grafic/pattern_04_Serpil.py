import turtle

Padme=turtle.Turtle()
turtle.bgcolor("black")
        #Sharpness & thikness of the printed lines
turtle.speed(10)
b=["blue","yellow","red","white","orange"]


for i in range (149):
    for a in b:
        Padme.color(a)
        Padme.forward(i*0.3)
        Padme.right(8)



turtle.done()