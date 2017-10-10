# CTI-110 
# M2HW2 - Tip Tax Total 
# De Jesus Jose
# September 18, 2017
# Calculate the total cose of a meal with tax and tip.

#Variables
FoodCost = float(input("Enter the cost of your food: "))
TipAmount = FoodCost * 0.18
SalesTax = FoodCost * 0.07
TotalCost = FoodCost + SalesTax
TotalCostWithTip = FoodCost + TipAmount + SalesTax

# Display the Tip, Tax, TotalCost
print("The Sales Tax is:", format(SalesTax, ",.2f"))
print("The Tip Amount is:", format(TipAmount, ",.2f"))
print("The Total Cost is:", format(TotalCost, ",.2f"))
print("The Total Cost with Tip is:", format(TotalCostWithTip, ",.2f"))
