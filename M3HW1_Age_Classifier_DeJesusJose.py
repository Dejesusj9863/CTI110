# CTI-110 
# M3HW1 - Age Classifier 
# Jose De Jesus 
# september 28, 2017
# Create a program that asks the user to enter a person’s age.
# Then displays if the person is an:
# infant, a child, a teenager, or an adult.


def Main():


    # User inputs age in years
    Age = float(input("Type in the age of person: "))

    # Decisions to find if Age equals infant, child, teen or adult
    if Age <= 1:
        print("That person is an infant.")

    elif Age > 1 and Age <13:
        print("That person is a child.")

    elif Age >= 13 and Age < 20:
        print("That person is a teenager.")

    elif Age >= 20:
        print("That person is an adult.")

# Program start
Main()
Main()
Main()
Main()

