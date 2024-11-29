# Exercise: https://github.com/codebasics/py/blob/master/Basics/Exercise/23_sets_frozensets/23_sets_frozensets.md
# Q1
vowels = ['a','e','i','o','u']
set_1 = frozenset(vowels)
print(set_1) 
# Q2
set1 = frozenset({1,2,3,4,5})
set2 = frozenset({4,5,6,7,8})
print(f"Difference between set1 and set2 is {set1.difference(set2)}")