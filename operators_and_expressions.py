milk_per_serving = 1.5 #1.5 cups
scoops_per_serving = 3 #3 scoops
total_guests =2 

# Multuply to calculate the total ingredients needed for the total guests
total_milk_needed = milk_per_serving * total_guests #3.0 cups
total_scoops_needed = scoops_per_serving * total_guests #6 scoops

#Subtract to find the remaining inventory
#remaining_milk = 12.0 - total_milk_needed #9.0 cups

milk_ounces = 16
pour_amount = 6
remaining = milk_ounces - pour_amount
print(remaining)