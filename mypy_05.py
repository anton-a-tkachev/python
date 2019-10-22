# Functions
import math

# Define a function
def volume(r):
    """Returns the volume inside a sphere of the given radius"""
    return (4/3)*math.pi*r**3

# Two default arguments
def cm(feet = 0, inches = 0):
    """Converts length from imperic to metric units"""
    return 12*2.54*feet + 2.54*inches

# One required argument and two default arguments
def mag(x, y = 0, z = 0):
    """Returns the magnitude of the given radius-vector"""
    return math.sqrt(x**2 + y**2 + z**2)

print(volume(3))

print(cm(feet = 1))
print(cm(feet = 1, inches = 1))
print(mag(-1))
print(mag(-10,2,5))