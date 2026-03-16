msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""
print(msg , quote)

my_str = "Hello world"
print("Hello" in my_str) #True
print("Hey" in my_str) #False
print("hi" in my_str) #false
print("e" in my_str) #true
print("f" in my_str) #False

my_str = "Hello world"
print(len(my_str)) #11
print(my_str[6])#w
print(my_str[0])#H
print(my_str[-1])#d
print(my_str[-3])#r

#String Concatination
my_str_1 = "Hello"
my_str_2 = "World"
str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str)# Hello World

#name = 'John Doe'
#age = 26
#name_and_age = name + age
#print(name_and_age)#TypeError: Can only concatinate str (not "int") to str

name = 'John Doe'
age = 26
name_and_age = name + str(age)
print(name_and_age)# John Doe26

name = 'John Doe'
age = 26
name_and_age = name #Start with name 
name_and_age += str(age) #Append the age as string
print(name_and_age) #John Doe26

#f-strings interpolation
name = "John Doe"
age = 26
name_and_age = f"My name is {name} and i am {age} years old"
print(name_and_age) #My name is John Doe and i am 26 years old

num1 = 5
num2 = 10
print(f"The sum of {num1} and {num2} is {num1 + num2}")#The sum of 5 and 10 is 15

#String Slicing (This doesn't alter original str)
#syntax     string[start:stop]
my_str='Hello World'
print(my_str[1:4])# ell

print(my_str[:7])# Hello w

print(my_str[8:])# rld

print(my_str[:])# Hello World

#Apart from 'start' 'stop' indices, theres also an optional 'step' parameter, which is used to specify the increment between each index in the slide as shown bellow
# syntax   string[start:stop:step]
print(my_str[0:11:2])# Hlowrd

# A trick to reverse a string is having step as -1 and start and stop empty
print(my_str[::-1]) #dlrow olleH


#String Methods
#upper()
uppercase_my_str = my_str.upper()
print(uppercase_my_str) #HELLO WORLD

#lower()
lowercase_my_str = my_str.lower()
print(lowercase_my_str) #hello world

#strip
my_str = '  hello Nick      '
trimmed_my_str = my_str.strip()
print(trimmed_my_str)# "hello Nick"

#replace(old, new)
replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)# hi Nick

#split(separator)
my_str = 'Hello world'
split_words = my_str.split()
print(split_words)#['hello', 'world']

#join(iterable)
my_list = ['hello', 'world']
joined_my_str = ''.join(my_list)
print(joined_my_str)#hello world

#startswith(prefix)
my_str = 'hello world'
starts_with_hello = my_str.startswith('hello')
print(starts_with_hello) #True

