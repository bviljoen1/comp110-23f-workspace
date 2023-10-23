"""Turtle - A Working Masterpiece."""
__author__ = "730579443"


from turtle import Turtle, colormode, tracer, update, done
import random

colormode(255)
bob: Turtle = Turtle()


def main() -> None:
    """The enttrypoint of my scene."""
    tracer(0, 0)

    # Create a turtle for drawing the night sky background
    background: Turtle = Turtle()
    draw_night_sky(background, -400, -400, 675)

    # Create a turtle for snow capped mountains
    mountain: Turtle = Turtle()
    draw_mountain(mountain, -325, -275)
    draw_mountain(mountain, -400, -250)

    # Create a turtle for drawing the dark green grass
    grass: Turtle = Turtle()
    draw_grass(grass, -400, -400)

    # Create a turtle for snowcaps on top of front brown mountains
    snowcap: Turtle = Turtle()
    draw_snowcap(snowcap)

    # Create a turtle for drawing 50 randomly placed stars in the night sky.
    star: Turtle = Turtle()
    draw_star()
    
    # Create a turtle for drawing the moon. needs to be two circled, one white one black eclipsed.
    white_moon: Turtle = Turtle()
    draw_white_moon(white_moon, -250, 150, 50)

    # Create a turtle for drawing the black moon at coordinates to overlap white moon.
    black_moon: Turtle = Turtle()
    draw_black_moon(black_moon, -225, 150, 50)

    update()
    done()


def draw_night_sky(background: Turtle, x: float, y: float, width: float) -> None:
    """Draw the black rectangle that will act as the night sky."""
    background.penup()
    background.goto(-400, -400)
    background.pendown()
    background.speed(0)
    background.color("black")
    background.fillcolor(0, 0, 0)

    background.begin_fill()
    idx: int = 0
    while idx < 2:
        background.forward(975)
        background.left(90)
        background.forward(1000)
        background.left(90)
        idx += 1
    background.end_fill()


def draw_grass(grass: Turtle, x: float, y: float) -> None:
    """Draw the dark green grass at the bottom of the screen that spans the entire ngiht sky."""
    grass.penup()
    grass.goto(-400, -400)
    grass.pendown()
    grass.speed(0)
    grass.color("green")
    grass.fillcolor(6, 101, 12)

    grass.begin_fill()
    for i in range(2):
        grass.forward(975)
        grass.left(90)
        grass.forward(150)
        grass.left(90)
    grass.end_fill()


def draw_mountain(mountain: Turtle, x: float, y: float) -> None:
    """Draws 6 brown mountains in the background too seem far away."""
    mountain.penup()
    mountain.goto(x, y)
    mountain.pendown()
    mountain.speed(0)
    mountain.color("gray")
    mountain.pencolor(102, 51, 0)
    mountain.fillcolor(102, 51, 0)

    for i in range(6):
        mountain.begin_fill()
        for a in range(6):
            mountain.forward(150)
            mountain.left(120)
        mountain.end_fill()
        mountain.forward(150)


def draw_snowcap(snowcap: Turtle) -> None:
    """Draw white triangles as snow caps on the front brown mountains."""
    snowcap.penup()
    snowcap.goto(-345, -155)
    snowcap.color("white")
    snowcap.pencolor("white")
    snowcap.fillcolor("white")
    snowcap.speed(0)
    snowcap.hideturtle()
    
    for c in range(6):
        snowcap.begin_fill()
        for d in range(3):
            snowcap.forward(40)
            snowcap.left(120)
        snowcap.end_fill()
        snowcap.forward(150)


def draw_star() -> None:
    """Will Draw 50 stars, each is 5-pointed and the same size, but they will be placed at random coordinates (x,y) in the night sky."""
    star: Turtle = Turtle()
    star.pencolor("white")
    star.fillcolor("white")
    star.penup()
    star.color("white")
    star.speed(0)
    star.pendown()
    star.hideturtle()

    for a in range(50):
        star.penup()
        x = random.randint(-400, 475)
        y = random.randint(-125, 600)
        star.goto(x, y)
        star.pendown()
        star.begin_fill()
        for i in range(5):
            star.forward(10)
            star.right(144)
        star.end_fill()


def draw_white_moon(white_moon: Turtle, x: float, y: float, radius: float) -> None:
    """Draws white circle at called upon coordinates (x,y) to create a circular moon shape. This will be turned into a crescent using an overlapping black circle."""
    white_moon.speed(0)
    white_moon.color(225, 229, 235)
    white_moon.pencolor(225, 229, 235)
    white_moon.fillcolor(225, 229, 235)
    white_moon.penup()
    white_moon.goto(x, y)
    white_moon.pendown()
    white_moon.begin_fill()
    white_moon.circle(50)
    white_moon.end_fill()


def draw_black_moon(black_moon: Turtle, x: float, y: float, radius: float) -> None:
    """Draws white circle that overlaps the white circle to create a crescent moon shape."""
    black_moon.speed(0)
    black_moon.color(0, 0, 0)
    black_moon.pencolor(0, 0, 0)
    black_moon.fillcolor(0, 0, 0)
    black_moon.penup()
    black_moon.goto(x, y)
    black_moon.pendown()
    black_moon.begin_fill()
    black_moon.circle(50)
    black_moon.end_fill()


if __name__ == "__main__":
    main()

done()