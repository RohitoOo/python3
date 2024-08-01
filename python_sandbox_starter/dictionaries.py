# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# Create Dictionary

person = {
    'first_name' : "Rohito",
    'last_name' : "Rohito",
    'age' : 30,
}
person2 = {
    'first_name' : "Jacob",
    'last_name' : "AAA",
    'age' : 32,
}

print(person['age'])
print(person.get('age'))

# get dick keys 

print(person.keys())

# get dick items

print(person.items())

print(len(person2))

print((person2.items))



