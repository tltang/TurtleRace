# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# import turtle
# from turtle import Turtle, Screen
import turtle as t
import random

my_screen = t.Screen()
my_screen.setup(width=500, height=400)
colors = ["lime green", "red", "blue", "purple", "orange", "yellow"]
user_bet = my_screen.textinput(f"Make your bet", f"Which turtle will win the race? ({colors}). Enter a color: ")
turtles = []
iY = 0
winner = ""

def move_forwards(turtle, step):
    turtle.forward(step)

for i in range(6):
    iY = iY + 30
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[i - 1])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + iY)
    new_turtle.pendown()
    turtles.append(new_turtle)

if user_bet:
    lContinue = True

while lContinue:
    for turtle in turtles:
        step = random.randint(1, 10)
        move_forwards(turtle, step)
    # turtle size = 40 * 40
        if turtle.xcor() > 230:
            lContinue = False
            winner = turtle.pencolor()

if winner == user_bet:
    print(f"You win! {winner} turtle won the race.")
else:
    print(f"You lose! {winner} turtle won the race.")

# def move_backwards():
#     new_turtle.backward(5)
#
# def move_counterclock():
#     current_heading = new_turtle.heading() + 5
#     new_turtle.setheading(current_heading)
#
# def move_clock():
#     current_heading = new_turtle.heading() - 5
#     new_turtle.setheading(current_heading)
#
# def move_home():
#     new_turtle.clear()
#     new_turtle.penup()
#     new_turtle.home()
#     new_turtle.pendown()

my_screen.listen()
# my_screen.onkey(key="space", fun=move_forwards)
# my_screen.onkey(key="w", fun=move_forwards)
# my_screen.onkey(key="s", fun=move_backwards)
# my_screen.onkey(key="a", fun=move_counterclock)
# my_screen.onkey(key="d", fun=move_clock)
# my_screen.onkey(key="c", fun=move_home)


my_screen.exitonclick()

