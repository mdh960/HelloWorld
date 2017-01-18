# connect the Turtle and random libraries (aka "modules")
import turtle, random
import time
import math

wn = turtle.Screen()
wn.bgcolor('black')

# let's make a turtle
tina = turtle.Turtle()
tina.speed(0)

# list of colors
colors = ["cyan", "violet", "yellow", "orange", "blue", "red", "hot pink", "silver", "aqua", "lime", "white"]


# random color picker
def color_tina():
    pick = random.randint(0, len(colors) - 1)
    tina.color(colors[pick])


def crazy(size):
    color_tina()
    tina.forward(size)
    tina.right(120)
    tina.forward(size)
    tina.right(120)
    tina.forward(size)
    tina.right(120)


def crazy2(size):
    color_tina()
    tina.forward(size)
    tina.left(120)
    tina.forward(size)
    tina.left(120)
    tina.forward(size)
    tina.left(120)


'''
  tina.forward(size)
  tina.right(100)
'''


def star(size):
    color_tina()
    tina.forward(size)
    tina.right(100)
    tina.forward(size)
    tina.left(100)


# let's make some methods, like plays in a playbook
def square(some_turtle):
    # stop writing
    some_turtle.penup()
    # go to the middle
    some_turtle.goto(0, 0)
    # start writing
    some_turtle.pendown()
    # go up
    some_turtle.goto(0, 50)
    # go right
    some_turtle.goto(50, 50)
    # go down
    some_turtle.goto(50, 0)
    # go back to the start
    some_turtle.goto(0, 0)

    # draw a series of circles, size = size of first circle


def super_circles(size):
    for x in range(1, 11):
        color_tina()
        tina.circle(size * x)


for x in range(-10, -100, -5):
    crazy(x)

'''
# let's make tina draw that square
# she'll fill in the spot of "some_turtle"
square(tina)

# let's draw a circle in the middle
tina.goto(25,0)
tina.circle(25)

#call my fancy new function
super_circles(5)
'''
tina.penup()
tina.pendown()

# AT THE END OF MY APP I WILL USE A CONDITIONAL

while True:
    answer = input("Do you want to see more?(Yes/No)")
    print("You just said: " + answer)
    if answer == "No":
        print("Okay, your loss")
    elif answer == "Yes":
        print("Have fun!")
        while True:
            tina.penup()
            tina.goto(random.randint(-150, 150), random.randint(-150, 150))
            tina.pendown()
            for x in range(-10, -100, -5):
                crazy(x)
            tina.penup()
            tina.goto(random.randint(-150, 150), random.randint(-150, 150))
            tina.pendown()
            for x in range(-10, -100, -5):
                crazy2(x)
    elif answer == "yes":
        print("Have fun!")
        while True:
            tina.penup()
            tina.goto(random.randint(-150, 150), random.randint(-150, 150))
            tina.pendown()
            for x in range(-10, -100, -5):
                crazy(x)
            tina.penup()
            tina.goto(random.randint(-150, 150), random.randint(-150, 150))
            tina.pendown()
            for x in range(-10, -100, -5):
                crazy2(x)
    elif answer == "no":
        print("Okay, your loss")
    else:
        print("What?")


