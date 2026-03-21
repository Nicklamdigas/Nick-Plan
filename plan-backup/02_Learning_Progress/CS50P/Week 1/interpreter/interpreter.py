x, operator, z = input("Enter your number and opertator: ").split()
num1 = float(x)
num2 = float(z)
if operator == "+":
    print(f" {num1 + num2}")
elif operator == "-":
    print(f" {num1 - num2}")
elif operator == "*":
    print(f"{num1 * num2}")
elif operator == "/":
    if num2 != 0:
        print(f"{num1 / num2}")
    else:
        print("Error: Division by zero.")        
else:
    print("Invalid Operator")