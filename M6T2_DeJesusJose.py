# CTI - 110
# Jose De Jesus
# November 21, 2017
# A value-returning function, converting feet to inches


# Main function 
def main():
    # User input for feet
    feet = int(input("Enter a number of feet: "))

    # Created an if statement in the case that they use one foot
    # So it does not say feet in the output
    if feet > 1:
         # Using return fuction to make a conversion
         print(feet, "feet equals", Conversion(feet), "inches")

    else:
        # Using return fuction to make a conversion
        print(feet, "foot equals", Conversion(feet), "inches")

# Converts Feet to inches
def Conversion(feet):
          return feet * 12

# Program start
main()
