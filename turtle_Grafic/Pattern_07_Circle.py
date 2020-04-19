import turtle

turtle.bgcolor("yellow")
turtle.pensize(4)          #Sharpness & thikness of the printed lines
turtle.speed(0)
b=["red","blue","green","purple"]
for i in range(9):
    for a in b:
        turtle.color(a)
        turtle.circle(100)   #radios of circle
        turtle.left(10)      #distance between each circles
turtle.mainloop()