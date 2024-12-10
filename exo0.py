total_people = int(input("How many people need a ride? "))
people_per_taxi = int(input("How many people fit in one taxi? "))
full_taxis = total_people // people_per_taxi

if total_people % people_per_taxi > 0:
    total_taxis = full_taxis + 1
else:
    total_taxis = full_taxis
print(f"Number of taxis needed: {total_taxis}")