#In this workshop, you will practice working with numbers and mathematical operations to build a bill splitter. This tool will calculate how much each person owes after adding meal costs and a tip.

#To start, you need a way to keep track of the total amount as costs are added. In Python, you can use a variable to store an integer (a whole number) that changes over time.

running_total = 0
num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

running_total += appetizers + main_courses + desserts + drinks
print(f"Total bill so far: {running_total}")

tip = running_total * 0.25
print(f"Tip amount: {tip}")

running_total += tip
print(f"Total with tip: {running_total}")

final_bill = running_total / num_of_friends
print(f"Bill per person: {final_bill}")

each_pays = round(final_bill,2)
print(f"Each person pays: {each_pays}")