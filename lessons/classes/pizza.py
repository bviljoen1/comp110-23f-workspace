"""Defining a class!"""

# tells mf to stop bitching about the types when defining the pizza at the bottom
from __future__ import annotations

"""
Think of a class definition as a roadmap for
objects that belong to the class
you are defining the underlying structure
every instance of this class we will have
"""


class Pizza:
    """This is my class to represent pizza!"""
    
    # attributes
    # syntax: <name> : <type>
    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, size_input: str, toppings_input: int, gf_input: bool):
        self.size = size_input
        self.toppings = toppings_input
        self.gluten_free = gf_input
        # returns self

    def price(self) -> float:
        """Method to compute price of pizza"""
        if self.size == "large":
            cost: float = 6.25
        else:
            cost: float = 5.00
        cost += 0.75 * self.toppings
        if self.gluten_free:
            cost += 1.00
        return cost
    

    def add_toppings(self, num_toppings: int):
        """Update existing pizza order with num_toppings."""
        self.toppings += num_toppings


    def add_toppings_new_order(self, num_toppings: int) -> Pizza:
        """Make a new pizza order using existing info."""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings, self.gluten_free)
        return new_pizza
    
    def __str__(self) -> str:
        """The result when I call str()."""
        pizza_info: str = f"Pizza Order: {self.toppings} toppings, size {self.size}, GF: {self.gluten_free}."
        return pizza_info

my_pizza: Pizza = Pizza("medium", 3, False)
print(str(my_pizza))
sals_pizza: Pizza = Pizza("large", 1, True)
print(str(sals_pizza))