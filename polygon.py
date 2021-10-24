from turtle import Turtle, Screen

t = Turtle()
scr = Screen()
t.penup()
t.home()
t.pendown()
for sides in range(3, 11):
    angle = 360 / sides
    for j in range(sides):
        t.forward(150)
        t.right(angle)

t.hideturtle()
scr.exitonclick()
