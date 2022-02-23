"""A series of functions intended to create a starry night inspired bell tower scene -- it's like he even painted it himself ;) !"""

from turtle import Turtle, colormode, done, tracer, update

"""7. In the bell function definition (ln 111 - 164), i broke down the creation of the bell tower into muiltiple, subsequent while loops/functions as opposed to my first instinct which was to create one loop within which to create all the individual shapes of the shapes."""
"""8. Implemented the circle() turtle function in order to create the moon (ln 70), crescent shape (ln 86), and its halo (ln 54)."""
"""8. Within the main function definition, i imported random integers (ln 196 - 208) in order to crearte a randomized pattern of stars for my night sky."""
"""I noticed after finishing my code that there was more from Professor Jordan in which he described the "setheading" and "draw_square" calls so my code does not implement those since I decided not to go back and redo my code."""

__author__ = "730440093"

sky: Turtle = Turtle()
light: Turtle = Turtle()
moon: Turtle = Turtle()
crescent: Turtle = Turtle()
star: Turtle = Turtle()
tower: Turtle = Turtle()
time: Turtle = Turtle()


def night_sky(davinci: Turtle, x: float, y: float) -> None:
    """Function to draw frame and fill in background color of night sky."""
    davinci.hideturtle()
    davinci.speed(50)
    davinci.penup()
    davinci.goto(x, y)
    davinci.pendown()

    colormode(255)
    davinci.fillcolor(35, 48, 103)
    davinci.pencolor(35, 48, 103)

    davinci.begin_fill()
    i: int = 0 
    while (i < 4):
        davinci.fd(500)
        davinci.left(90)
        i += 1
    davinci.end_fill()


def moon_light(davinci: Turtle, x: float, y: float) -> None:
    """Function to create halo of moonlight in which the moon will be palced."""
    davinci.hideturtle()
    davinci.speed(50)
    davinci.penup()
    davinci.goto(x, y)
    davinci.pendown()

    colormode(255)
    davinci.color(250, 250, 170)

    davinci.begin_fill()
    davinci.circle(55)
    davinci.end_fill()


def moon_itself(davinci: Turtle, x: float, y: float) -> None:
    """Function to create full moon within halo."""
    davinci.hideturtle()
    davinci.speed(50)
    davinci.penup()
    davinci.goto(x, y)
    davinci.pendown()

    colormode(255)
    davinci.color(240, 240, 40)

    davinci.begin_fill()
    davinci.circle(30)
    davinci.end_fill()


def crescent_moon(davinci: Turtle, x: float, y: float) -> None:
    """Function to carve hole in full moon to create illusion of crescent moon."""
    davinci.hideturtle()
    davinci.speed(50)
    davinci.penup()
    davinci.goto(x, y)
    davinci.pendown()

    colormode(255)
    davinci.color(250, 250, 170)

    davinci.begin_fill()
    davinci.circle(20)
    davinci.end_fill()
    

def stars(davinci: Turtle, x: int, y: int, len: int) -> None:
    """Base function of singular star creation."""
    davinci.hideturtle()
    davinci.speed(200)
    davinci.penup()
    davinci.goto(x, y)
    davinci.pendown()

    colormode(255)
    davinci.color(250, 250, 170)

    i: int = 0
    side_len: float = len
    while (i < 60):
        davinci.tilt(90)
        davinci.fd(side_len)
        davinci.left(170) 
        side_len *= 0.97   
        i += 1   


def bell(davinci: Turtle, x: float, y: float) -> None:
    """Function which stacks shapes upon one another in order to create the bell tower."""
    davinci.hideturtle()
    davinci.speed(50)
    davinci.penup()
    davinci.goto(x, y)
    davinci.pendown()

    colormode(255)
    
    i: int = 0
    p: int = 0 
    t: int = 0 

    davinci.color(255, 205, 155)
    davinci.begin_fill()
    davinci.goto(x, y + 60)
    while (i < 2):
        davinci.fd(70)
        davinci.left(90)
        davinci.fd(300)
        davinci.left(90)
        i += 1
    davinci.end_fill()

    davinci.color(200, 200, 200)
    davinci.begin_fill()
    davinci.goto(-205, y)
    while (p < 2): 
        davinci.fd(130)
        davinci.left(90)
        davinci.fd(60)
        davinci.left(90)
        p += 1 
    davinci.end_fill()

    davinci.penup()
    davinci.goto(x, 110)
    davinci.pendown()
    davinci.color(200, 200, 200)
    davinci.begin_fill()
    while (t < 3):
        davinci.fd(70)
        davinci.left(120)
        t += 1
    davinci.end_fill()

    davinci.color(220, 220, 220)
    davinci.penup()
    davinci.goto(-140, 50)
    davinci.pendown()
    davinci.begin_fill()
    davinci.circle(25)
    davinci.end_fill()


def clock(davinci: Turtle, x: float, y: float) -> None:
    """Function to install the time within the circle(clock) of the bell tower."""
    davinci.hideturtle()
    davinci.speed(50)
    davinci.penup()
    davinci.goto(x, y)
    davinci.pendown()

    colormode(255)
    davinci.color("black")

    davinci.goto(-118, 80)

    davinci.penup()
    davinci.goto(x, y)
    davinci.pendown()

    davinci.goto(-140, 87)


def main() -> None:
    """Function to paint picture!"""
    tracer(0, 0)
    night_sky(sky, -250, -250)
    moon_light(light, 180, 115)
    moon_itself(moon, 180, 140)
    crescent_moon(crescent, 190, 155)
    bell(tower, -175, -250)
    clock(time, -140, 72)
    from random import randint
    left_side: int = 0
    right_side: int = 0
    while left_side < 5:
        l_x_placement: int = randint(-250, -180)
        l_y_placement: int = randint(-250, 250)
        stars(star, l_x_placement, l_y_placement, 10)
        left_side += 1
    while right_side < 25:
        r_x_placement: int = randint(-115, 250)
        r_y_placement: int = randint(-250, 250)
        stars(star, r_x_placement, r_y_placement, 10)
        right_side += 1
    update()
    done()


if __name__ == "__main__":
    main()