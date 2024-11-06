# Exercise: https://github.com/codebasics/py/blob/master/Basics/Exercise/5_lists/5_lists_exercise.md

# Q1=> 
exp = [2200, 2350, 2600, 2130, 2190]
print(f"1> In feb I spent {exp[1]-exp[0]} dollars more compared to january")
print(f"2> My total expense in first 3 months is {exp[0]+exp[1]+exp[2]}")
print(f"3> Did I spent 2000 dollars in any month? {2000 in exp}")
exp.append(1980)
print(f"4> Added June expense: {exp}")
x = 200+exp[4]
print(f"5> Corrected expense of april: {x}")

# Q2=> 
heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.append('black panther')
print(f"2> Added black panther to the list: {heros}")
heros.remove('black panther')
heros.insert(3,'black panther')
print(f"3> Added black panther after hulk {heros}")
heros[1:3]=['doctor strange']
print(f"4> Replaced thor and hulk with doctor strange")
heros.sort()
print(f"5> Sorted list: {heros}")