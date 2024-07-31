# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods


name = 'Rohito'

age = 35

# Concatenate 

# print('Hello my name is '+ name + 'and my age is' +str(age))

# String Formatting

# Arguments by positioning 
# print('My name is {name} and I am {age}'.format(name=name, age=age))

# Fstring   
print(f'hello my name is {name} and I am {age}')

# String Methods

s = 'hello world'

# Capitalize string 

print(s.capitalize())
print(s.upper())
print(len(s))