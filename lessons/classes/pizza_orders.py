"""Instantiating A Class."""

"""
This is where we instantiate the class
we defined in classes.py
in other words, were creating objects 
that belong to that class.
"""

# import the class
# from <file name>.<module name> import <class>
from lessons.classes.pizza import Pizza


"""my_pizza: Pizza = Pizza()""" # Constructor <- Constructing a new pizza
# make arguments in the pizza above
my_pizza: Pizza = Pizza("Large", 10, True) # Cosntructor

# access/set/update attribute values
# my_pizza.size = "large"
# my_pizza.toppings = 10
# my_pizza.gluten_free = True
my_pizza.toppings += 2

print("Size: ")
print(my_pizza.size)
print(my_pizza.toppings)

# print("my_pizza: ")
# print(my_pizza)

# print("Pizza class: ")
# print(Pizza)

# make sals_pizza size medium, 5 toppings, NOT GF

sals_pizza: Pizza = Pizza("medium", 5, False)
print("Sals Bitchass pizza: ")
print(sals_pizza.size)
print(sals_pizza.toppings)
print(sals_pizza.gluten_free)

def price(input_pizza: Pizza) -> float:
    """Function to compute the price of a pizza."""
    if input_pizza.size == "large":
        cost: float = 6.25
    else:
        cost: float = 5.00
    cost += 0.75 * input_pizza.toppings
    if input_pizza.gluten_free:
        cost += 1.00
    return cost

# Calling the function.
print(price(my_pizza))
print(price(sals_pizza))


# Calling the method.
print(my_pizza.price())
print(sals_pizza.price())

my_pizza.add_toppings(3)
print(my_pizza.toppings)
print(my_pizza.price())

my_second_pizza: Pizza = my_pizza.add_toppings_new_order(2)
print(my_second_pizza.toppings)
print(my_pizza.toppings)