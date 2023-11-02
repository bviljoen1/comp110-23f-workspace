"""Practice for my own benefit"""
"""EX02 - One Shot Wordle - A step toward Wordle."""
__author__ = "730579443"

secret_word: str = "python"
word_length: int = len(secret_word)
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
emoji: str = ""
character_idx: int = 0
wrong_spot: bool = False
alt_idx: int = 0

guess: str = input(f"What is your {word_length}-letter guess? ")

while len(guess) != word_length:
    guess = input(f"That was not {word_length} letters! Try again: ")

  
i: int = 0
n: int = 0
exists = False

while i < word_length:
    if guess[i] == secret_word[i]:
        emoji += GREEN_BOX
        i += 1
    #If current index being checked does NOT equal secret word index
    #Secret Word = python, Guess = photo
    else:
        n = 0
        exists = False
        while exists == False and n < word_length:
            if secret_word[n] == guess[i]:
                exists = True
                emoji += YELLOW_BOX
                i += 1
            else:
                n += 1
                if n == word_length:
                    emoji += WHITE_BOX
                    i += 1

print(emoji)

while len(guess) == word_length and guess != secret_word:
    print("Not Quite. play again soon!")
    exit()
if guess == secret_word:
    print("Woo! you got it!")