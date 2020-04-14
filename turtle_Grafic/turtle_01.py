from turtle import *

hideturtle()
dot(60)
goto(100, 100)
begin_fill()
pencolor("red")
dot(20)
forward(100)
pencolor('blue')
right(200)
dot(50)
pencolor('orange')
right(100)
goto(90,10)
pencolor('green')
dot(30)
goto(150,-40)
fillcolor('yellow')
end_fill()
dot(60)

circle(80)
pencolor('red')
circle(100)




up()
goto(0, -50)
down()
fillcolor('red')
circle(50)
end_fill()

up()
goto(0, -100)
down()
fillcolor('yellow')
circle(100)
end_fill()

up()
goto(0, -150)
down()
fillcolor('green')
circle(150)
end_fill()

up()
goto(0, -200)
down()
fillcolor('magenta')
circle(200)
end_fill()

goto(80, 80)
pencolor('blue')
for i in range(4):
    circle(40+i*5)