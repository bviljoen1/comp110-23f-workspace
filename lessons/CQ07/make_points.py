"""Make Points docstring."""
from lessons.CQ07.point import Point

fortnite_point: Point = Point(2.0, 3.0)

fortnite_point.scale_by(2)
print(fortnite_point.x, fortnite_point.y)

# print(fortnite_point.scale_by(3))
# print(fortnite_point.scale(3))

new_point: Point = fortnite_point.scale(3)
print(new_point.x, new_point.y)