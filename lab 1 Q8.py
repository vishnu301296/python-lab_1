
import random
ranum= random.randint(1, 9)

guess = int(input("Enter a guess number : "))

if guess < ranum:
        print("Too Low")
elif guess > ranum:
        print("Too High")
else:
        print("Exactly Right!")