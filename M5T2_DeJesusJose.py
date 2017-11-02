# CTI 110
# M5T2 - Bug Collector
# Jose De Jesus
# October 5, 2017
# Calculate the total number of bugs collected during a seven day period.

# Imports time for time.sleep()
import time

def main():

    # Variables
    TotalDays = 7
    TotalNumberOfBugs = 0

    # Loop question repeated for the seven days
    for CurrentDay in range(1, TotalDays + 1):
        BugsCollected = int(input("How many bugs were collected on day " + str(CurrentDay) + ":"))

        # Adding all the bugs collected each day
        TotalNumberOfBugs = TotalNumberOfBugs + BugsCollected

    time.sleep(2)

    print()
    # Displaying the total number of bugs collected through the week
    print("The total number of bugs collected for all", TotalDays, "days is", TotalNumberOfBugs)

# Learned this part from a code I saw online about a game asking if you wanted to play again

PlayAgain = 'yes'
while PlayAgain == 'yes' or PlayAgain == 'y':
    # Program Start
    main()
    
    print('Would you like to start next weeks report? (yes or no)')
    PlayAgain = input()
    print() 
