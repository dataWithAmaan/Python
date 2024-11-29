# Exercise: https://github.com/codebasics/py/blob/master/Basics/Exercise/22_list_set_dict_comprehension/22_list_set_dict_comprehension.md
# Q1
integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]
binary_dict = {x: y for (x,y) in zip(integer, binary)}
print(binary_dict) 

# Q2
integer2 = [1, -1, 2, 3, 5, 0, -7]
additive_inverse = list(map(lambda a:-a, integer2))
print(additive_inverse)

# Q3
integer3 = [1, -1, 2, -2, 3, -3]
sq_set = {i*i for i in integer3}
print(sq_set)