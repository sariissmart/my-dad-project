# the program should start by generating a random number between 1 and 100 (inclusive). This will be the number that the player has to guess.
# 2. The program should then prompt the player to enter their guess.
# 3. If the player's guess is too high, the program should print a message saying "Too high! Try again."
# 4. If the player's guess is too low, the program should print a message saying "Too low! Try again."
# 5. If the player guesses the correct number, the program should print a message saying "Congratulations! You guessed the number."
# 6. The game should continue until the player guesses the correct number.
import random
a = random.randint(1, 100)
user = int(input("Choose a number between 1 to 100"))
if user == a:
    print("Congratulations! You guessed the number", user, "and the correct answer is", a, )
else:
    while a!=user:
        if user > a:
            print("Too high! Try again")
        elif user < a:
            print("Too low! Try again.")
        user = int(input("Choose a number between 1 to 100"))
        if user == a:
            print("Congratulations! You guessed the number", user, "and the correct answer is", a, )
            break
        






