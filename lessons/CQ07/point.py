"""Challenge question 07."""

from __future__ import annotations

__author__ = "730579443"


class Point:
    """Class to represent Point."""

    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Init function that does the thing."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Function that multiplies the x and y by a constant."""
        self.x *= factor
        self.y *= factor

    new_x: float
    new_y: float

    def scale(self, factor: int) -> Point:
        """Function that creates a new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point