# CTI - 110 
# M6HW1 - Test Average and Grade
# Jose De Jesus
# November 21, 2017
# Program asks the user to enter five test grades,
# then outputs the numerical grade and letter grade in a table,
# and also prints the test average.


# Gets test scores from user and calls dertermin_grade() and calc_average()
def main():
    # asks for user to unput their FIVE test scores
    Score_1 = float(input("Enter Score 1: "))
    Score_2 = float(input("Enter Score 2: "))
    Score_3 = float(input("Enter Score 3: "))
    Score_4 = float(input("Enter Score 4: "))
    Score_5 = float(input("Enter Score 5: "))

    # Makes a table with the numerical and letter grades
    determine_grade(Score_1, Score_2, Score_3, Score_4, Score_5)
    
    # Calculates the average test score the user made
    calc_average(Score_1, Score_2, Score_3, Score_4, Score_5)
    
# Makes a table with the numerical and letter grades
def determine_grade(Score_1, Score_2, Score_3, Score_4, Score_5):
    # Starts table
    print("scores \t\tNumeric grade \t\tLetter Grade")
    print("--------------------------------------------------------------")
    # Data in the table is displayed (numerical and letter grade) and evenly spaced
    print('Score 1:', '\t', format(Score_1, ',.1f'), "\t\t\t" ,LetterGrade1(Score_1, Score_2, Score_3, Score_4, Score_5))
    print('Score 2:', '\t', format(Score_2, ',.1f'), "\t\t\t" ,LetterGrade2(Score_1, Score_2, Score_3, Score_4, Score_5))
    print('Score 3:', '\t', format(Score_3, ',.1f'), "\t\t\t" ,LetterGrade3(Score_1, Score_2, Score_3, Score_4, Score_5))
    print('Score 4:', '\t', format(Score_4, ',.1f'), "\t\t\t" ,LetterGrade4(Score_1, Score_2, Score_3, Score_4, Score_5))
    print('Score 5:', '\t', format(Score_5, ',.1f'), "\t\t\t" ,LetterGrade5(Score_1, Score_2, Score_3, Score_4, Score_5))
    # Ends table
    print("--------------------------------------------------------------")

##############################################################    
### I couldn't figure out how to write the lettergrade() part
### in a loop so I just wrote it out one by one :(
##############################################################

# Calculates the letter grade using the user's input score
def LetterGrade1(Score_1, Score_2, Score_3, Score_4, Score_5):
    A_score = 89.5
    B_score = 79.5
    C_score = 69.5
    D_score = 59.5
    F_score = 59.4                                                                                                

    # once the number grade makes a true statement it returns the letter grade
    if Score_1 >= A_score:
        return('A')        
    elif Score_1 >= B_score:
        return('B')
    elif Score_1 >= C_score:
        return('C')
    elif Score_1 >= D_score:
        return('D')
    elif Score_1 <= F_score:
        return('F')

# Calculates the letter grade using the user's input score
def LetterGrade2(Score_1, Score_2, Score_3, Score_4, Score_5):
    A_score = 89.5
    B_score = 79.5
    C_score = 69.5
    D_score = 59.5
    F_score = 59.4                                                                                                


    if Score_2 >= A_score:
        return('A')        
    elif Score_2 >= B_score:
        return('B')
    elif Score_2 >= C_score:
        return('C')
    elif Score_2 >= D_score:
        return('D')
    elif Score_2 <= F_score:
        return('F')
# Calculates the letter grade using the user's input score
def LetterGrade3(Score_1, Score_2, Score_3, Score_4, Score_5):
    A_score = 89.5
    B_score = 79.5
    C_score = 69.5
    D_score = 59.5
    F_score = 59.4                                                                                                


    if Score_3 >= A_score:
        return('A')        
    elif Score_3 >= B_score:
        return('B')
    elif Score_3 >= C_score:
        return('C')
    elif Score_3 >= D_score:
        return('D')
    elif Score_3 <= F_score:
        return('F')
# Calculates the letter grade using the user's input score
def LetterGrade4(Score_1, Score_2, Score_3, Score_4, Score_5):
    A_score = 89.5
    B_score = 79.5
    C_score = 69.5
    D_score = 59.5
    F_score = 59.4                                                                                                


    if Score_4 >= A_score:
        return('A')        
    elif Score_4 >= B_score:
        return('B')
    elif Score_4 >= C_score:
        return('C')
    elif Score_4 >= D_score:
        return('D')
    elif Score_4 <= F_score:
        return('F')
# Calculates the letter grade using the user's input score
def LetterGrade5(Score_1, Score_2, Score_3, Score_4, Score_5):
    A_score = 89.5
    B_score = 79.5
    C_score = 69.5
    D_score = 59.5
    F_score = 59.4                                                                                                


    if Score_5 >= A_score:
        return('A')        
    elif Score_5 >= B_score:
        return('B')
    elif Score_5 >= C_score:
        return('C')
    elif Score_5 >= D_score:
        return('D')
    elif Score_5 <= F_score:
        return('F')
# Calculates the average score in both numerical value and a letter grade
def calc_average(Score_1, Score_2, Score_3, Score_4, Score_5):

    # Total score formula
    total_score = Score_1 + Score_2 + Score_3 + Score_4 + Score_5
    # Average score formula
    Average_score = total_score/5
    # prints the values and alligns them to the table
    print('Average score: \t', format(Average_score, ',.1f'), "\t\t\t" ,LetterGrade6(Average_score))
    
# Calculates the letter grade using the Average_score
def LetterGrade6(Average_score):
    A_score = 89.5
    B_score = 79.5
    C_score = 69.5
    D_score = 59.5
    F_score = 59.4                                                                                                


    if Average_score >= A_score:
        return('A')        
    elif Average_score >= B_score:
        return('B')
    elif Average_score >= C_score:
        return('C')
    elif Average_score >= D_score:
        return('D')
    elif Average_score <= F_score:
        return('F')
# program start    
main()
