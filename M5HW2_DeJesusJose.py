# CTI 110
# M5HW2 - Running Total
# Jose De Jesus
# October 12, 2017
# user enters numbers and once the user inputs a negative number
# the program will stop asking and then add the numbers excluding the negative


def main():

    # Variables
    total = 0
    sum = 0

    # User input for number
    inputnum = float(input("Enter a number? "))
            
    # While loop for inputnum
    while inputnum >= 0:

        # Sum of all inputs, excluding the negative
        sum = sum + inputnum
        inputnum = float(input("Enter a number? "))
        
    print()
    # Total sum of inputted numbers
    print("Total:         ", format(sum, ',.2f'))

# Program Start
main()

