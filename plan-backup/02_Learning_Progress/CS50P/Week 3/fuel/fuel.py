while True:
    user_input = input("Enter your fraction: ").strip()

    try:
        fuel_level = user_input.split("/")
        numerator = int(fuel_level[0]) 
        denominator = int(fuel_level[1])

        if numerator > denominator:             #Logic Error
            print("Invalid input: Denominator must be greater than Numerator")
            continue
        elif denominator == 0 :                 #ZeroDivisionError
            print("Cannot divide by zero 0")
            continue
        elif numerator < 0 or denominator < 0:
            print("Use a positive number")
            continue
        else:
            break
    except (ValueError, ZeroDivisionError):
        print("Invalid input. Try again.")



fuel_level_Percentage = round((numerator/denominator)*100)
if fuel_level_Percentage <= 1:
    print("E")
elif fuel_level_Percentage >= 99:
    print("F")
else:
    print(f"{fuel_level_Percentage}%")

