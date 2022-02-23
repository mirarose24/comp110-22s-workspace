from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
bob: Turtle = Turtle()

leo.speed(50)
leo.hideturtle()

bob.speed(50)
bob.hideturtle()


leo.penup()
leo.goto(45, 60)
leo.pendown()

bob.penup()
bob.goto(45, 60)
bob.pendown()

colormode(255)
leo.color(200, 200, 200)
bob.pencolor("black")


# leo.begin_fill()
# i: int = 0 
# while (i < 3): 
#     leo.forward(200)
#     bob.forward(200)
#     leo.left(120)
#     bob.left(120)
#     i += 1
# leo.end_fill()

side_len: float = 200

i: float = 0 
while (i < 100): 
    bob.forward(side_len)
    bob.left(122)
    side_len *= 0.97
    i += 1


done()
