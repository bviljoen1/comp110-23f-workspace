"""Program that loops until correct number is guessed."""

from random import randint

# Secret number will be a random number between 1-10. 
secret: int = randint(1,10)
guess: int = int(input("Guess a number between 1 and 10: "))
# input returns a string, must put int() before to fix this.
number_of_tries: int = 0
max_tries: int = 3

while (guess != secret) and (number_of_tries < max_tries):
    print("Wrong!")
    # if guess is out of bounds, let them know.
    if (guess < 1) or (guess > 10):
        print("That is not between 1 and 10!")
    if guess < secret:
        print("Too low!")
        # hints
        guess = int(input("Guess again: "))
    number_of_tries += 1
    print("You have used " + str(number_of_tries) + " tries. You have " + str(max_tries - number_of_tries) + " left!")
    else:
        print("Too high!")
        # hints
        # could use "elif" 

    # ask for a different guess. changes the value of guess to re-evaluate in the while statement.
    guess = int(input("Guess again: "))
    number_of_tries += 1
    print("You have used " + str(number_of_tries) + " tries. You have " + str(max_tries - number_of_tries) + " left!")

# after you guess correctly, while condition will be false --> it will exit the while loop
if guess == secret:
    print("Correct! Great guess!")
else:
    print("You lose! >:( ")
