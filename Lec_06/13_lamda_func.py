# lamda functions (extra study) 
# resource: https://www.freecodecamp.org/news/python-lambda-functions/

'''Syntax:
lambda arguments: expression'''

add = lambda a,b: a+b
print(add(5,7)) 

# Map function

'''Syntax:
map(function, iterable)'''

numbers = [1,2,3,4,5]
square = list(map(lambda x: x**2, numbers))
print(square)

# Filter function

'''Syntax:
filter(function, iterable)'''

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) 

# How to use lambda functions with the sorted function

'''Syntax:
sorted(iterable, function)'''

employees = [{"name": "John", "age": 32},{"name": "Jane", "age": 27},{"name": "Jim", "age": 40}]
sorted_employees = sorted(employees, key=lambda x: x["age"])
print(sorted_employees)

'''When to Use key in Sorting Functions
The key parameter can be useful with other functions that involve ordering or finding max/min values, such as sorted(), min(), and max().'''

employees = [{"name": "John", "age": 32},{"name": "Jane", "age": 27},{"name": "Jim", "age": 40}]
sorted_employees = max(employees, key=lambda x: x["age"])
print(sorted_employees)