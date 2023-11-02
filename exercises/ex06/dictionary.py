"""Dictionaries. Working Progress."""
__author__ = "730579443"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of two strings, [str1, str2] will return them reversed order [str2, str1]."""
    result_dict = {}

    for key in input_dict:
        value = input_dict[key]
        if value in result_dict:
            raise KeyError("Error: Duplicate key in the inputted Dictionary.")
        
        result_dict[value] = key

    return result_dict


# Using their examples to test if it works as it should
input_dict = {'apple': 'cat'}
result = invert(input_dict)
print(result)


# This one is confusing as heck.


def favorite_color(name_colors: dict[str, str]) -> str:    
    """Takes a dictionary of peoples names and their favorite color and will return the most popular colour."""
    number_colours: dict[str, int] = {}  # Empty Dictionary that will store each color with the number of times it appears.
    popular_color: str = ""
    max_number = 0

    for name in name_colors:
        color = name_colors[name]
        if color in number_colours:
            number_colours[color] += 1
        else:
            number_colours[color] = 1
        
        if number_colours[color] > max_number:
            popular_color = color
            max_number = number_colours[color]
    
    return popular_color


# Example usage:
name_colors = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
result = favorite_color(name_colors)
print(result)


def count(count_list: list[str]) -> dict[str, int]:
    """Produces a dictionary that stores the values from the list as well as how many times those vlaues appears."""
    empty_dict: dict[str, int] = {}

    for elem in count_list:
        if elem in empty_dict:
            empty_dict[elem] += 1
        else:
            empty_dict[elem] = 1
    return empty_dict


my_list: list[str] = ["apple", "banana", "apple", "cherry", "banana", "banana", "fortnite"]
result4 = count(my_list)
print(result4)


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Categorize a list into a dictionary that stores the first letter with the words that staart with that letter."""
    empty_dict: dict[str, list[str]] = {}

    for word in input_list:
        first_letter = word[0].lower()

        if first_letter in empty_dict:
            empty_dict[first_letter].append(word)
        else: 
            empty_dict[first_letter] = [word]

    return empty_dict


words: list[str] = ["cat", "apple", "boy", "angry", "bad", "car"]
result5 = alphabetizer(words)
print(result5)


def update_attendance(input_dict: dict[str, list[str]], weekday: str, student: str) -> dict[str, list[str]]:
    """Takes an existing dictionary consisting of the day of the week and students names. returns a attendance log of each weekday and the students in attendance."""
    if weekday in input_dict:
        input_dict[weekday].append(student)
    else:
        input_dict[weekday] = [student]
    
    return input_dict


# Attendance dict.
attendance_log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
update_attendance(attendance_log, "Tuesday", "Vrinda")
update_attendance(attendance_log, "Wednesday", "Kaleb")
print(attendance_log)