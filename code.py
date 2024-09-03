import random

num =random.randint(1, 100)
guess =int(input("Guess a number between 1 and 100:"))

while guess != num:
    if guess < num:
        print("Too low. Try again.")
    elif guess > num:
        print("Too high. Try again.")
        
    guess = int(input("Guess a number between 1 and 100:"))
    
print("your Guess is right.")
