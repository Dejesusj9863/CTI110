# CTI 110
# M5HW1 - Distance Traveled
# Jose De Jesus
# October 10, 2017
# User inputs both speed and time (hours) and the program will
# Display the distance traveled each hour traveled in a table format.


def program():

    #user imput for speed and time
    Speed = float(input("What was the speed of the vehivle in MPH? "))

    Time = float(input("How many hours has it traveled? "))

    print()


    # Table starts
    print("Hour(s) \tDistance Traveled(In Miles)")

    print("-------------------------------------------")


    # Looped while 
    Hours = 0
    while Hours < Time:
        Hours = Hours + 1
        # Variable
        Distance = Speed * Hours
        print(Hours,'\t \t', format(Distance, ',.2f'))

'''
    # Looped for
    for Hours in range(1, Time + 1):
        # Variable
        Distance = Speed * Hours
        print(Hours, '\t' ,format(Distance, ',.2f'))
'''



# Program Start
program()
print()
print()
program()

