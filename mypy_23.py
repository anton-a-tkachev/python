# Using unit tests
from math import pi

def circle_area(r):
    if type(r) not in [int, float]: raise TypeError("Type of input must be either <int> or <float>")
    if r < 0: raise ValueError("The radius cannot be negative")
    return pi*r**2

# radii = [2, 0, -3, 2 + 5j, True, "radius"]

# message = "Area of a circle wiht r = {radius} is {area}"

# [print(message.format(radius = r, area = circle_area(r))) for r in radii]