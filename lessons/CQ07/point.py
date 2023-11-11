"""Challenge question 07."""

from __future__ import annotations

__author__ = "730579443"


class Point:
    """Class to represent Point."""

    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Init function that does the thing."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: float) -> None:
        """Function that multiplies the x and y by a constant."""
        self.x *= factor
        self.y *= factor

    new_x: float
    new_y: float

    def scale(self, factor: float) -> Point:
        """Function that creates a new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self) -> str:
        """Function that returns the coordinates of x,y."""
        point_string: str = f"x: {self.x}; y: {self.y}"
        return point_string
    
    def __mul__(self, factor: int | float) -> Point:
        """Function that multiplies known point and creates a new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __add__(self, factor: int | float) -> Point:
        """Adds x to y and creates a new point."""
        new_point: Point = Point(self.x + factor, self.y + factor)
        return new_point