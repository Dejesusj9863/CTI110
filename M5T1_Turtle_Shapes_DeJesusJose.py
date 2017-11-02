# CTI 110
# M5T1 - Initials
# Jose De Jesus
# October 13, 2017
# Create Shapes with turtle

import turtle                           # Allows me to use turtles
wn = turtle.Screen()                    # Creates a playground for turtles
wn.bgcolor("black")                     # Set the window background color
wn.title("SI VIS PACEM PARA BELLUM")    # set the window title
                                        # (latin: if you want peace, prepare for war)
hannah = turtle.Turtle()                # Creates turtle named hannah
hannah.color("red")                     # Changes turtle color to red
hannah.shape("circle")                  # Changes turtle's shape
sarai = turtle.Turtle()                 # Creates turtle named sarai
sarai.color("blue")                     # Changes turtle color to blue
sarai.shape("arrow")                    # Changes turtle's shape


for x in range(4):                      # Makes a Square in a for loop
    hannah.forward(100)
    hannah.right(90)

sarai.left(90)                          # Orientates the turtle

for y in range(2):
    sarai.forward(200)
    sarai.left(90)
    sarai.forward(100)
    sarai.left(90)

wn.mainloop()


