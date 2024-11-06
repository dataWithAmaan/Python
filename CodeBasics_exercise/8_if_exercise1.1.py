# Exercise: https://github.com/codebasics/py/blob/master/Basics/Exercise/8_if/8_exercise_description.md

# Q1i=> 
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
city = input("Enter city name: ")
if city in india:
    print("City is in India")
elif city in pakistan:
    print("City is in Pakistan")
elif city in bangladesh:
    print("City is in bangladesh")    
else:
    print("Invalid city")
    