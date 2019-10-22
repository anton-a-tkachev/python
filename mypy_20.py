# Map, Filter and Reduce

import math

def area(r):
    """Returns the area of a circle of radius r"""
    return math.pi*r**2

radii = [1,2,3,4,5]

# Mapping with direct method
# areas = []
# for r in radii:
#     areas.append(area(r))
# print(areas)

# Mapping with map function

# print(map(area,radii))  # is an iterator object
print(list(map(area,radii)))    # is the list

temps = [
    ("Berlin", 29),
    ("Cairo", 36),
    ("Buenos Aires", 19),
    ("Los Angeles", 26),
    ("Tokyo", 27),
    ("New York", 28),
    ("London", 22),
    ("Beijing", 32) 
]
print("Temperature in Farenheits:")
print(list(map(lambda data: (data[0], 9/5*data[1] + 32), temps)))
print()

# Filtering data with filter function
import statistics

avg = statistics.mean([data[1] for data in temps])
print("The average temperature is",avg)
print("The list of cities with temperature above average:")
print(list(filter(lambda data: data[1] > avg, temps)))

# Filtering out empty data
countries = [
    "",
    "Argentina",
    "",
    "Brazil",
    "Chilie",
    "",
    "Columbia",
    "",
    "Ecuador",
    "",
    "",
    "Venezuela"
]

# print(list(filter(lambda s: s != "", countries)))
print(list(filter(None, countries)))    # does the same
