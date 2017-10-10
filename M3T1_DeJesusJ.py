# CTI-110
#M2T1 - Areas of Rectangles
# Jose De Jesus
# 09/21/2017
# A program that asks for the length and width of two rectangles.

# Variables for Rectangle One
Rec_L1 = float(input('Enter the length of Rectangle One: '))
        
Rec_W1 = float(input('Enter the width of Rectangle One: '))

Rec_A1 = Rec_L1 * Rec_W1

# Variables for Rectangle Two
Rec_L2 = float(input('Enter the length of Rectangle Two: '))

Rec_W2 = float(input('Enter the width of Rectangle Two: '))

Rec_A2 = Rec_L2 * Rec_W2

# Little extra thing to make it look like it's taking some time ( I know it'll execute fast but still... I thought it would be cool)
print("Calculating the results...")


# Decisions 
if Rec_A1 == Rec_A2:
              print("Both areas are equal")
elif Rec_A1 > Rec_A2:
              print("The area of Rectangle One is grester than Rectangle Two")
elif Rec_A1 < Rec_A2:
              print("The area of Rectangle One is less than Rectangle Two")
              
