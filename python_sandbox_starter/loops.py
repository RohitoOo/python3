# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Paul', "S", "Z", "AAA"]

# for person in people :
#     print(f'Current Person', person)
    
    
# for person in people :
#     if person == 'Z':
#         break
#     print(f'1. Current Person', person)
    
    
# for person in people :
#     if person == 'Z':
#         continue
#     print(f'2. Current Person', person)
    
    
# for i in people :
    
#     print(f'Current Person', i)
#     print (i)
    
for i in range(0,  8) :
    
    print(f'Number :', i)

# While loops execute a set of statements as long as a condition is true.


count = 0 

while count <= 10 :
    print(f'Count {count}')
    count += 1
