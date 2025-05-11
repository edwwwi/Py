import turtle
t=turtle.Turtle()
t.pencolor("green")
def hexagon(t, length):
    for count in range(6):
        t. forward(length)
        t.left(60)
def draw_circle(t,n,length):
    for count in range(n):
        hexagon(t,length)
        t.left(360/n)
        t.showturtle()
draw_circle(t, 10, 50)
t.turtledone()