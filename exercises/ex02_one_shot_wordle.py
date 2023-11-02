"""EX02 - One Shot Wordle - A step toward Wordle."""
__author__ = "730579443"

secret_word: str = "python"
word_length: int = len(secret_word)
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
emoji: str = ""

# ask user to input a guess. the secret word will determine the number associated with the question... if the word "hello" is secret, then the length is 5 and the question will ask for a 5-letter word
guess: str = input(f"What is your {word_length}-letter guess? ")

# as long as the length of the guess does NOT equal the length of secret, the question will be repeated until user provides a 6 letter guess.
while len(guess) != word_length:
    guess = input(f"That was not {word_length} letters! Try again: ")

# defining variables used in part 2 and 3
character_idx: int = 0
alt_idx: int = 0
wrong_spot: bool = False

# as long as the character index being checked is less than word length, if it matches then a GREEN box will print in that index spot.
while character_idx < word_length:
    if guess[character_idx] == secret_word[character_idx]:
        emoji += GREEN_BOX
        character_idx += 1
# If current index that is being checked does NOT equal the secret word index then it comes here

    else:
        alt_idx = 0
        wrong_spot = False
        # defining an alternate index (part 3) and a boolean (part 3) to be used to make yellow boxes.
        while not wrong_spot and alt_idx < word_length:
            # if the bool is false (preset) and the alternate index is less than the word length, the If/else statements will continue until this is false, thus ending the while loop
            if secret_word[alt_idx] == guess[character_idx]:
                wrong_spot = True
                emoji += YELLOW_BOX
                character_idx += 1
                # ABOVE: if the secret word at alternate index = guess word at ANY INDEX, then a yellow box will be printed. stating that the letter is present, just not in that place (index)
            else:
                alt_idx += 1
                # ABOVE: if a letter in the guess word is not found in the secret word, a yellow box WILL NOT print, and it will go to the "else" statement where the alternate index will increase by 1, allowing the loop to try again to find yellow circles.
                # If Letter in Guess is NOT in secret, a white box will print and the loop restarts to look for matching letters at character index of the guess.
                if alt_idx == word_length:
                    emoji += WHITE_BOX
                    character_idx += 1

# this will print all the boxes (Green, White, Yellow) to show which letters are where and which are not etc. the emoji variable is defined as empty "" which means when we say += GREEN_BOX then it will add a green box to the emoji variable.
# printing this emoji variable will concatenate all the boxes we've created up until here.
print(emoji)

# If you write the correct number of letters but the wrong word, it will print the respective boxes, then say "not quite, play again"

if len(guess) == word_length and guess != secret_word:
    print("Not quite. Play again soon!")

# if you guess correctly it will print both the green boxes, AND a "Woo! you got it!"
if guess == secret_word:
    print("Woo! You got it!")