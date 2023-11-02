from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

# Moves pen somewhere before it continues drawing
leo.penup()
leo.goto(-300, -300)
leo.pendown()
# choses color of pen
leo.pencolor("pink")
leo.fillcolor(0, 0, 0)
leo.color(66, 193, 20)

leo.speed(50)
leo.hideturtle()

leo.begin_fill()
i: int = 0
while (i < 6):
    leo.forward(300)
    leo.left(60)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()

bob.penup()
bob.goto(-300, -300)
bob.pendown()

bob.pencolor("black")
bob.color(0, 0 , 0)

bob.speed(1000)
bob.hideturtle()

side_length: int = 300
i: int = 0
while (i < 120):
    bob.forward(side_length)
    bob.left(60)
    side_length = side_length * 0.9999
    i += 1
done()