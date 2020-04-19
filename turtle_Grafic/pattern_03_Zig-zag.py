import turtle

Padme=turtle.Turtle()

        #Sharpness & thikness of the printed lines
turtle.speed(10)



for i in range (20):
        if(i%2==0):
            Padme.forward(i * 2)
            Padme.right(120)
        else:
            Padme.forward(i * 2)
            Padme.left(120)




turtle.done()