user_input = input("Enter your phrase: ")
vowels = ["a","e","i","o","u","A","E","I","O","U"]

result = ""
for char in user_input:
    if char not in vowels:
        result += char

print(result)