import turtle
from turtle import *
from random import randint

john=Turtle()
bob=Turtle()
sally=Turtle()

john.color('red')
bob.color('blue')
sally.color('green')

john.penup()
john.goto(-140,140)
john.pendown()

bob.penup()
bob.goto(-140,100)
bob.pendown()

sally.penup()
sally.goto(-140,60)
sally.pendown()

for movement in range(10):
    john.forward(randint(1,50))
    bob.forward(randint(1,50))
    sally.forward(randint(1,50))

turtle.done()
# The newturtle.py code creates three turtles, each with a different color.
# The turtles are named john, bob, and sally.
# The turtles are placed at different starting positions on the screen.
# The turtles move forward a random distance between 1 and 5 units.
# The turtles move forward 10 times.
# The turtle.done() function keeps the turtle window open.
# The turtle.done() function is necessary to keep the turtle window open.
