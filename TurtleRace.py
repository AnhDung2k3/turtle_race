from turtle import Turtle, Screen
from random import randint

start_race = False

display = Screen()
#setup to resize
display.setup(600, 400)

#display the dialog box to select
user_choice = display.textinput(title = "Select the lucky turtle", prompt= "Choose the color of turtle:")

turtle_color = ["red", "orange", "yellow", "green", "blue", "purple"]

if user_choice:
    start_race = True

#Create a list of turtle
turtle_list = []

distance = 0

for i in range(6):
    me = Turtle(shape = "turtle")
    me.color(turtle_color[i]) 
    me.penup()
    distance += 50
    #goto to set up the position
    me.goto(x = -280, y = -160 + distance)
    turtle_list.append(me)

while start_race:
    for turtle_each in turtle_list:
        #xcor to get the value of x_axis of object
        if turtle_each.xcor() >= 260:
            start_race = False
            #get the color of object that appropriate to color
            win_color = turtle_each.pencolor()
            if win_color == user_choice:
                print("You win !")
            else:
                print("You lose, try again !")
        step = randint(1, 10)
        turtle_each.forward(step)

display.exitonclick()