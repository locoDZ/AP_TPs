
TICKET_PRICE = 15.50
name = input("Please enter your name: ")
if name == "VIP":
    print("Enjoy the show for free!")
else:
    num_tickets = int(input("How many tickets would you like to buy? "))
    total_cost = num_tickets * TICKET_PRICE
    print(f"The total cost is {total_cost}")
    print("Enjoy your tickets!")