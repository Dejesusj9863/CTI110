# CTI 110
# M5T1 - Initials
# Jose De Jesus
# October 19, 2017
# Create initials with turtle


import turtle                           # Allows me to use turtles
wn = turtle.Screen()                    # Creates a playground for turtles
wn.bgcolor("black")                     # Set the window background color
wn.title("SI VIS PACEM PARA BELLUM")    # set the window title
                                        # (latin: if you want peace, prepare for war)
frank = turtle.Turtle()                 # Creates turtle named frank
frank.color("red")                      # Changes turtle color to red
frank.shape("circle")                   # Changes turtle's shape



frank.forward(100)   
frank.backward(50)
frank.right(90)
frank.forward(100)                      # Creates the letter J 
frank.right(90)
frank.forward(50)

frank.penup()
frank.right(90)
frank.forward(100)
frank.right(90)
frank.forward(150)
frank.pendown()

frank.right(90)
frank.forward(100)
frank.left(90)
frank.forward(30)
frank.left(30)
frank.forward(30)
frank.left(60)                          # Creates the letter D
frank.forward(70)
frank.left(60)
frank.forward(30)
frank.left(30)
frank.forward(30)

# Ends commands
wn.mainloop()           # Wait for user to close window
