# In this project, I will be storing the names and prices of a 
# furniture store’s catalog in variables. I will then process 
# the total price and item list of customers, printing them to 
# the output terminal.

#Adding first item
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""
lovely_loveseat_price = 254.00

#Adding second item
stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
stylish_setttee_price = 180.50

#Adding the third item
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""
luxurious_lamp_price = 52.15

#Calculating sales tax
sales_tax = 0.088

#Customer one running tally of expenses
customer_one_total = 0

#Customer one list of descriptions of items being purchased
customer_one_itemization = ""

#Customer one purchases the lovely loveseat
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

#Customer one also purchases the luxurious lamp
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

#Customer one check out!
customer_one_tax = customer_one_total * sales_tax

#Adding sales tax to customer one total cost
customer_one_total += customer_one_tax

#Printing up customer one's receipt
print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)

