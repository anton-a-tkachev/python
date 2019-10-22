# Sorting

# Alkaline earth metals
earth_metals = [
    "Beryllium",
    "Magnesium",
    "Calcium",
    "Strontium",
    "Barium",
    "Radium"
]
earth_metals.sort()
print(earth_metals)
earth_metals.sort(reverse = True)
print(earth_metals)
print()

# Planets as tuples
planets = [
    ("Mercury", 2440, 5.43, 0.395),
    ("Venus", 6052, 5.24, 0.723),
    ("Earth", 6378, 5.52, 1.000),
    ("Mars", 3396, 3.93, 1.530),
    ("Jupiter", 71492, 1.33, 5.210),
    ("Saturn", 60268, 0.69, 9.551),
    ("Uranus", 25559, 1.27, 19.213),
    ("Neptune", 24764, 1.64, 30.070)
]

planets.sort(key = lambda planet: planet[1], reverse = True)
[print(planet) for planet in planets]
print()

# Planets as dictionaries
planets = [
    {"Name": "Mercury", "Radius": 2440,  "Density": 5.43, "Distance": 0.395},
    {"Name": "Venus",   "Radius": 6052,  "Density": 5.24, "Distance": 0.723},
    {"Name": "Earth",   "Radius": 6378,  "Density": 5.52, "Distance": 1.000},
    {"Name": "Mars",    "Radius": 3396,  "Density": 3.93, "Distance": 1.530},
    {"Name": "Jupiter", "Radius": 71492, "Density": 1.33, "Distance": 5.210},
    {"Name": "Saturn",  "Radius": 60268, "Density": 0.69, "Distance": 9.551},
    {"Name": "Uranus",  "Radius": 25559, "Density": 1.27, "Distance": 19.213},
    {"Name": "Neptune", "Radius": 24764, "Density": 1.64, "Distance": 30.070}
]

planets.sort(key = lambda planet: planet["Density"])
[print(planet) for planet in planets]
print()

# Calling sorted function - creates a sorted copy stored in a list
myset = {3,2,4,1,7,8,5,9,6,0}
print(sorted(myset))
print()

# Calling sorded on a string
mystr = "Here is a string"
print(sorted(mystr))
