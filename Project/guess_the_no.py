import random

target = random.randint(1,100)
print("Welcome to Guessing Game")
while True:
    userChoice = input("Guess the target or Quit : ")
    if(userChoice == "Quit"):
        print("Thanks for playing")
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("You guessed it!!")
        break
    elif(userChoice<target):
        print("your number is too small. Take a bigger guess..")
    else:
        print("your number is too big. Take a smaller guess..")

print("----GAME OVER----")