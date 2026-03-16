user = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

if user in ["42", "forty two", "forty-two"]:
    print ("Yes")
else: 
    print("No")