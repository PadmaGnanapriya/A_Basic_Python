import turtle

turtle.bgcolor("black")
turtle.pensize(7)          #Sharpness & thikness of the printed lines
turtle.speed(10)         #It create cricle drowing animation.
b=["blue","yellow","red","white","orange"]
for i in range(5):       #Limt the for loop.It stop over drowing
    for a in b:
        turtle.color(a)
        turtle.circle(120)   #radios of circle
        turtle.left(15)      #distance between each circles
turtle.mainloop()