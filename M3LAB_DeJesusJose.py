# CTI 110
# M3LAB
# Jose De Jesus
# September 26, 2017
# This program takes a number grade and outputs a letter grade.

def main():
    
    # System uses 10-point grading scale.
    A_score = 89.5
    B_score = 79.5
    C_score = 69.5
    D_score = 59.5
    F_score = 00.0
    

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
    elif score >= F_score:
        print('Your grade is: F')    

# program start
main()
