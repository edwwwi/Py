import turtle
n = int(input("enter number of sides"))
t = turtle.Turtle()
t.screen.bgcolor("red")
t.speed(1)
for i in range(n):
    t.right(360/n)
    t.forward(50)
turtle.done()