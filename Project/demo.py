import random
import string

def generate_secure_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

username = input("Enter your username: ")
password = input("Enter your password: ")

if len(password) < 8:
    ask = input("Your password is not secure. Would you like to automatically generate a password? (yes/no): ").strip().lower()
    if ask == "yes":
        password = generate_secure_password()
        print("Your new password is:", password)
    else:
        print("Please ensure your password is secure.")
else:
    print("Your password is secure.")