total_amount = float(input("Total amount: "))
num_items = int(input("Number of items: "))
day_of_week = input("Day of the week: ")

discount = 0
if day_of_week in ["Saturday", "Sunday"]:
    discount = 0.20
else:
    discount = 0.10
if num_items > 5:
    discount += 0.05
final_price = total_amount * (1 - discount)

print(f"Total price after discount: {final_price} dinars")