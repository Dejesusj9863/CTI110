# CTI 110
# M3LAB NESTED NESTED NESTED NESTED NESTED NESTED
# Jose De Jesus
# September 26, 2017
# This program takes a number grade and outputs a letter grade. 

'''
def main():
    
    # System uses 10-point grading scale.
    A_score = 89.5
    B_score = 79.5
    C_score = 69.5
    D_score = 59.5
    F_score = 59.4
    

    # user imputs score
    score = float(input('Enter score: '))

    # decisions 
    if score >= A_score:
        print('Your grade is: A')
        print("Awesome! Keep up the good work.")
    elif score >= B_score:
        print('Your grade is: B')
        print("Good job! Keep up the good work.")
    elif score >= C_score:
        print('Your grade is: C')
    elif score >= D_score:
        print('Your grade is: D')
    elif score <= F_score:
        print('Your grade is: F')    

# program start
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
'''




def mainNested():
    
    # System uses 10-point grading scale.
    A_score = 89.5 
    B_score = 79.5
    C_score = 69.5
    D_score = 59.5
    F_score = 59.4
    

    # user imputs score
    Score = float(input('Enter score: '))

    # decisions (NESTED)

    if Score >= D_score:
        print('Passing grade of: ')
        if Score >= A_score:
            print('A')
            print("Awesome! Keep up the good work.")
        elif Score >= B_score and Score < A_score:
            print('B')
            print("Good job! Keep up the good work.")
        elif Score >= C_score and Score < B_score:
            print('C')
            print("The school offers tutoring if you need it.")
        elif Score >= D_score and Score < C_score:
            print('D')
            print("Do you take notes?")        
    else:
        print('F')
        print("... See me after class!")



# program start
mainNested()
mainNested()
mainNested()
mainNested()
mainNested()
mainNested()
mainNested()
mainNested()
mainNested()
mainNested()




