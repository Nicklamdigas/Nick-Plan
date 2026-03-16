meal_cost = float(input("How much was your meal: ").replace("$", ""))
tip_added = float(input(" What percentage would you like to tip?: ").replace("%", ""))
tip = meal_cost *(tip_added / 100)
print(f"leave ${tip:.2f}")

#total_cost = meal_cost + (int meal_cost * int 100 + (tip_added/100))
#print(total_cost)