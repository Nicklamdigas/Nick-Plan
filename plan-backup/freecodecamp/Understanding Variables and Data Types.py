name = "John Doe" #Python knows this is a string
age = 25 #Python knows this is an integer

#Data Types
#Integer:A whole number without decimals, for example 10 or -5
my_integer_var = 10
print("Integer:", my_integer_var) #Integer: 10

#Float:A number with a decimal point, like 4.42or -0.5
my_float_var = 4.50
print("Float:", my_float_var) #FLoat: 4.5

#String:A sequence of characters enclosed in single or double quotation marks like "hello world!"
my_string_var = "Hello"
print("String:", my_string_var) #String: hello

#Boolean : A true o false type, written as True or False
my_boolean_var = True
print("Boolean:", my_boolean_var) #Boolean: True

#Set:An unordered collection of unique elements like {4,2,0}
my_set_var = {7,5,8}
print("Set:", my_set_var) #Set: {7,5,8}

#Dictionary: A collection of key-value pairs enclosed in curly braces, like {"name": "John Doe", "age": 28}
my_dictionary_var: dict[str, Any] = {'name': 'Alice', 'Age': 25} #I;m not sure why im getting this error but ill figure it out
print('Dictionary:', my_dictionary_var) #Dictionary: {"name": "Alice", "age": 25}

#Tuple: AN immutable ordered collection , enclosed in bracketsm like (7,8,4)
my_tuple_var = (7,5,8)
print("Tuple:", my_tuple_var) #Tuple: (7,5,8)

#Range: A sequence of numbers, oftenused in loops for example[5]
my_range_var = range(5)
print('Range:', my_range_var)#Range: range(0,5)

#list: An ordered collection of elemenets that supports different data types.
my_list = [22,"Hello World!", 3.14, True]
print(my_list)# [22, "hello world", 3.14,True]

#None: A special value that represents the absence of a value.
my_none_var = None
print("None:", my_none_var) #None: None

#To get the data type of a variable, you can use th type() function
my_var_1 = "Hello world"
my_var_2 = 21

print(type(my_var_1)) #<class 'str'>
print(type(my_var_2)) #<class 'int'>