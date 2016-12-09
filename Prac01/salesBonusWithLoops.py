__author__ = 'jc449799'


"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
choice = int(input("Enter any +ve number to continue or -ve to exit: "))
while choice > 0:
    sales = float(input("Enter sales: $"))
    if sales < 1000:
        bonus = sales / 10
    elif sales >= 1000:
        bonus = sales * (15/100)
    print(bonus)
    choice = int(input("Enter any +ve number to continue: " ))
print("Thank you.")