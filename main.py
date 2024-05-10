import random
import time

jokes = [
    "Why don't scientists trust atoms? Because they make up everything.",
    "How do you organize a space party? You planet.",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Why don't skeletons fight each other? They don't have the guts."
]

def tell_joke_recursive():
    """ Recursive function that continuously displays jokes. """
    print(random.choice(jokes))
    time.sleep(0.1)
    tell_joke_recursive()

def tell_joke_interactive():
    """ Recursive function for manual joke generation. """
    user_input = input("Type '1' to hear another joke or '2' to stop: ")
    if user_input == "1":
        print(random.choice(jokes))
        tell_joke_interactive()
    elif user_input == "2":
        print("Goodbye")
    else:
        print("Invalid input, please type '1' or '2'.")
        tell_joke_interactive()

def tell_joke_continuous():
    """ Function that continuously displays jokes without stopping. """
    while True:
        print(random.choice(jokes))
        time.sleep(0.1)

def tell_joke_manual():
    """ Function for manual joke generation. """
    while True:
        user_input = input("Type '1' to continue or '2' to stop: ")
        if user_input == "1":
            print(random.choice(jokes))
        elif user_input == "2":
            print("Goodbye")
            break
        else:
            print("Invalid input, please type '1' or '2'.")

print("Welcome to my joke generator.")
user_choice = input("Type '1' for automatic joke generation with recursion, Type '2' for manual joke generation with recursion, Type '3' for automatic joke generation, and Type '4' for manual joke generation. *Note: If you choose recursion it will eventually crash. Also, if you choose automatic there will be no stop option.*: ")

if user_choice == "1":
    tell_joke_recursive()
elif user_choice == "2":
    tell_joke_interactive()
elif user_choice == "3":
    tell_joke_continuous()
elif user_choice == "4":
    tell_joke_manual()
else:
    print("Invalid selection, please restart the program and select a valid option.")
