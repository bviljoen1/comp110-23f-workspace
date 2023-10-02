"""Wordle - A step toward a structured wordle."""
__author__ = "730579443"


# Contains character function definition
def contains_char(search_str: str, target_char: str) -> bool:
    """returns true or false for functions within"""
    assert len(target_char) == 1
    search_idx: int = 0
    while search_idx < (len(search_str)):
        if search_str[search_idx] == target_char:
            return  True
        else:
            search_idx += 1
    return False


# emojified function definition -> will see whether or not a character is present at each index
def emojified(first_guess: str, second_secret: str) -> str:
    """Codifies colored boxes for a guess based on a secret word using contains_char"""
    assert len(first_guess) == len(second_secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emojified_idx: int = 0
    emoji: str = ""
    # this below string will concatify the colored boxes depending on the user input.
    while emojified_idx < (len(first_guess)):
        if first_guess[emojified_idx] == second_secret[emojified_idx]:
            emoji += GREEN_BOX
        elif contains_char(second_secret, first_guess[emojified_idx]) == True:
            emoji += YELLOW_BOX
        elif contains_char(second_secret, first_guess[emojified_idx]) == False:
            emoji += WHITE_BOX
        emojified_idx += 1
    return emoji


def input_guess(expected_length: int) -> int:
    # this will make sure the inputted guess is the correct length as the expected. it will prompt usser to resubmit a word until it is the correct length
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """the entrypoint pf the program and main game loop."""
    # code goes here
    # the secret word is codes, undernearth it I am calling the functions I defined above to check each index of the word based on the input the user gives (guess_input)
    secret_word: str = "codes"
    guess_attempts: int = 1
    won: bool = False
    while guess_attempts < 7 and won == False:
        print(f"=== Turn {guess_attempts}/6 ===")
        guess = input_guess(5)
        print(emojified(guess, secret_word))
        if guess == secret_word:
            print(f"you won in {guess_attempts}/6 turns!")
            won = True
        else:
            guess_attempts += 1
        # if the person gets it wrong this will move it onto the next attempt.
    if won == False:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()