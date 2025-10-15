import random

rice_price = 45
sugar_price = 40
oil_price = 130

rice_qty = 3
sugar_qty = 2.5
oil_qty = 1.8

rice_total = rice_price * rice_qty
sugar_total = sugar_price * sugar_qty
oil_total = oil_price * oil_qty

total = rice_total + sugar_total + oil_total

total_int = int(total)
total_str = str(total_int)

delivery = random.randint(5, 10)
final = total_int + delivery
final_str = str(final)

print("Total bill (int): ₹", total_int)
print("Total bill (str): ₹" + total_str)
print("Delivery charge: ₹", delivery)
print("Final bill (int): ₹", final)
print("Final bill (str): ₹" + final_str)
 