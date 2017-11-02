# CTI 110
# M5T1 - Bonus
# Jose De Jesus
# October 19, 2017
# Create a snowflake with turtle 


import turtle                                       # Allows me to use turtles
wn = turtle.Screen()                                # Creates a playground for turtles
wn.bgcolor("lightblue")                             # Set the window background color
wn.title("SI VIS PACEM PARA BELLUM")                # set the window title
                                                    # (latin: if you want peace, prepare for war)
frank = turtle.Turtle()                             # Creates turtle named frank
frank.pensize(4)                                    # Pensize increase
frank.color("white")                                # Changes turtle color to red
frank.shape("turtle")                               # Changes turtle's shape


numFlakes = int(input("Number of flakes: "))        # Asks the user how many flakes they want


for i in range(numFlakes):                          # A for loop of how many flakes
    for i in range(2):                              # A for loop for the shape of the flake
        frank.forward(100)
        frank.right(60)
        frank.forward(100)
        frank.right(120)
    frank.right(360 / numFlakes)                    # This is so that the angle is consistant
                                                    # and makes it go all the way around

wn.exitonclick()
