__author__ = 'jc449799'

"""
A shipping company requires a small program that would allow them to quickly work out total shipping charge for a number
of items, each with different prices. The program allows the user to enter the number of items and the shipping cost for
each different item. Then the program computes and displays the total shipping cost. If the total shipping cost is over
$100, then a 10% discount is applied to the total shipping cost before the amount is displayed on the screen

"""
num_of_items = int(input("Number of items : "))
while num_of_items <= 0:
    print("number of items cannot be 0 or -ve please enter again")
    num_of_items = int(input("Number of items : "))
cost_per_item = float(input("Cost per each shipment : $ "))
total_cost = num_of_items * cost_per_item
if total_cost > 100:
    discount = total_cost/10
    total_cost -= discount
print("Total Cost for shipping {} items is $ {}".format(num_of_items,total_cost))