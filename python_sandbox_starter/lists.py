# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create a list 

numbers = [1,2,3,4,5]
fruits = ['A', "B", "C", "D"]


# Constructor
numbers2 = list((1,2,3,4,0))
print (numbers, numbers)

# Get a value  
print(fruits[0])

fruits.append('M')
fruits.insert(2,'L')

print(fruits)

fruits.pop(3)
fruits.sort(reverse=True)

print(fruits)