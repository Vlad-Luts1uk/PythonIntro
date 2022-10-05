import random

num = random.randint(1, 6)
guess = None

while guess != num:
    guess = input("Guess a Number Between 1 and 6: ")
    guess = int(guess)

    if guess == num:
        print("congratulations")
        break
    else:
        print("The Number Was", num)