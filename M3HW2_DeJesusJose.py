# CTI 110
# M3HW2 - Software Sales
# Jose De Jesus
# October 3, 2017
# Display the amount saved with discount
# and the total amount when discount is applied.

import time

def main():

    Total_Packages_Purchased = float(input("How many packages are you buying?: "))

    time.sleep(2)
    # I learned that this is how to make the code slow down and have a pause; 
    # So that the user can read each statement without feeling "rushed" as the code is being run.

    # Decisions
    if Total_Packages_Purchased < 10:

        Discount_00 = (99 * Total_Packages_Purchased)
        
        time.sleep(1) 

        print("Total Purchase Cost: $", format(Discount_00, ',.2f'))
        # For this if statement, I simplified it so I didnt have to do the extra line of code
        # Calculating the total ammount because it would be the same as the discount_00.
             
    elif Total_Packages_Purchased >= 10 and Total_Packages_Purchased <= 19:

        print("You've earned a 10% discount!")

        time.sleep(2)

        Discount_10 = ((99 * Total_Packages_Purchased) * 0.1)

        print("The amount you have saved with your discount is: $", format(Discount_10, ',.2f'))

        time.sleep(2)

        Cost_With_Discount_10 = ((99 * Total_Packages_Purchased) - Discount_10)

        print("Total Purchase Cost: $", format(Cost_With_Discount_10, ',.2f'))
                  
    elif Total_Packages_Purchased >= 20 and Total_Packages_Purchased <= 49:

        print("You've earned a 20% discount!")

        time.sleep(2)

        Discount_20 = ((99 * Total_Packages_Purchased) * 0.2)

        print("The amount you have saved with your discount is: $", format(Discount_20, ',.2f'))

        time.sleep(2)

        Cost_With_Discount_20 = ((99 * Total_Packages_Purchased) - Discount_20)

        print("Total Purchase Cost: $", format(Cost_With_Discount_20, ',.2f'))

    elif Total_Packages_Purchased >= 50 and Total_Packages_Purchased <= 99:

        print("You've earned a 30% discount!")

        time.sleep(2)

        Discount_30 = ((99 * Total_Packages_Purchased) * 0.3)

        print("The amount you have saved with your discount is: $", format(Discount_30, ',.2f'))

        time.sleep(2)

        Cost_With_Discount_30 = ((99 * Total_Packages_Purchased) - Discount_30)

        print("Total Purchase Cost: $", format(Cost_With_Discount_30, ',.2f'))

    elif Total_Packages_Purchased >= 100:

        print("~Congratulations~ You've earned a whopping 40% discount!")

        time.sleep(2)

        Discount_40 = ((99 * Total_Packages_Purchased) * 0.4)

        print("The amount you have saved with your discount is: $", format(Discount_40, ',.sf'))

        time.sleep(2)

        Cost_With_Discount_40 = ((99 * Total_Packages_Purchased) - Discount_40)

        print("Total Purchase Cost: $", format(Cost_With_Discount_40, ',.2f'))

main()
main()
main()
main()
main()
