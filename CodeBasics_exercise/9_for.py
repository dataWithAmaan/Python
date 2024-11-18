# Exercise: https://github.com/codebasics/py/blob/master/Basics/Exercise/9_for/9_for_exercise.md

# Q1=>
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0
for i in result:
    if i=="heads":
        count+=1
print(f"heads count = {count}") 

# # Q2=>
for i in range(1,11):
    if i%2!=0:
        print(i*i)

# Q3=>
expense_list = [2340, 2500, 2100, 3100, 2980]
month_names = ["Jan", "Feb", "March", "April", "May"]

expense_amt = int(input("Enter the amount: "))

found = False
for i in range(len(expense_list)):
    if expense_list[i] == expense_amt:
        print(month_names[i])
        found = True
        break

if not found:
    print("Invalid amount")

# Q4=>
for i in range(5):
    print(f"You ran {i+1} km")
    tired = input("Are you tired? ")
    if tired.lower() == "yes":
        print(f"You didn't finish the race. You ran {i+1} km.")
        break
else:
    print("Congratulations! You finished the 5 km race!")

# Q5=> https://www.youtube.com/watch?v=fX64q6sYom0
n = 5
for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()