# Product: Loveseat
# description
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

# price
lovely_loveseat_price = 254.00

# Product: Settee
# description
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

# price
stylish_settee_price = 180.50

# Product: Lamp
# description
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

# price
luxurious_lamp_price = 52.15

# sales tax is 8.8 %
sales_tax = 0.088

# Customer 1
customer_one_total = 0

customer_one_itemization = ""

# Customer 1 is buying our Loveseat
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

# Customer 1 is buying our lamp
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

# calculating sales tax for customer 1
customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax

# create a receipt
print("Customer One Items: ")
print(customer_one_itemization)
print("Customer One Total: ")
print(customer_one_total)