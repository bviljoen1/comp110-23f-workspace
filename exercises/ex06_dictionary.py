"""Dictionaries. Working Progress."""
__author__ = "730579443"


"""def invert(input_dict: dict[str1, str2]) -> dict[str2, str1]:"""

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

"""def favorite_color(input_dict: dict[str, str]) -> str:
    Takes a dictionary of names and their favorite colors. will return the most apparent favorite color.
    result_dict = {}
    color_idx: int = 0
    fav_color: str = ""


fav_color_input_dict = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
color_result = favorite_color(fav_color_input_dict)
print(color_result)"""


# FIX THIS SHIT..... REDO IT RAHHHHHH
def favorite_colors(name_colors: dict[str, str]) -> str:
    color_counts = {}  # A dictionary to store the count of each color
    most_popular_color = None
    max_count = 0

    for name in name_colors:
        color = name_colors[name]
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

        if color_counts[color] > max_count:
            most_popular_color = color
            max_count = color_counts[color]

    return most_popular_color

# Example usage:
name_colors = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "B2en": "red", "Be3n": "red", "Be4n": "red", "Be5n": "red", "Be6n": "red"}
result = favorite_colors(name_colors)
print(result)