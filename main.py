import time
from turtle import Turtle, Screen
from random import randint
scr = Screen()
scr.screensize(250, 250)

turtles = [Turtle() for i in range(7)]
turtles_colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
# start line and finish line
start = Turtle()
start.penup()
start.pensize(10)
start.pencolor('black')
start.goto(-180, -250)
start.pendown()
start.goto(200, -250)
start.hideturtle()

finish = Turtle()
finish.penup()
finish.pensize(10)
finish.pencolor('black')
finish.goto(-180, 250)
finish.pendown()
finish.goto(200, 250)
finish.hideturtle()

# starting positions
for index, t in enumerate(turtles):
    t.shape('turtle')
    t.setheading(90)
    t.penup()
    t.pensize(5)
    t.goto(-150 + index*50, -250)
    t.color(turtles_colours[index])
    t.pendown()

# move at random speed
running = True
while running:
    turtle_positions =[]
    for t in turtles:
        random_distance = randint(0, 30)
        if t.ycor() + random_distance >= 250:
            print(f'The {t.color()[0]} turtle won the race!')
            running = False
        t.forward(random_distance)
scr.exitonclick()

