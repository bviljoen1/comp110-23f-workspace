"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730579443"
random_word: str = input("Enter a 5-character word: ")
if len(random_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + single_character + " in " + random_word)

character_sum: int = 0
if random_word[0] == single_character:
    print(single_character + " found at index 0")
    character_sum += 1
if random_word[1] == single_character:
    print(single_character + " found at index 1")
    character_sum += 1
if random_word[2] == single_character:
    print(single_character + " found at index 2")
    character_sum += 1
if random_word[3] == single_character:
    print(single_character + " found at index 3")
    character_sum += 1
if random_word[4] == single_character:
    print(single_character + " found at index 4")
    character_sum += 1

if character_sum == 0:
    print("No instances of " + single_character + " found in " + random_word)
if character_sum == 1:
    print(str(character_sum) + " instance of " + single_character + " found in " + random_word)
if character_sum > 1:
    print(str(character_sum) + " instances of " + single_character + " found in " + random_word)
