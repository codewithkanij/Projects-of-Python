# Ask user if they want to generate a password or not
# If yes, ask for password length
# Generate password
# Print the password
# If initial response is no, exit program

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():                                                       # function define
    password_length = int(input("How long would you like your password to be? "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)  # eta na dile password er sob characters list er moto ['1','d','&','!'] erkm ashbe

    print(password)


option  = input("Do you want to generate a password ? (Yes/No)")




if option == "Yes":
    generate_password()                        # function call
elif option == "No":
    print("Program ended")
    quit()
else:
    print("Invalid input.Please input Yes or No")
    quit()