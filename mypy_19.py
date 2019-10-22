# Lambda expressions

scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", 
"Arthur C. Clarke", "Frank Herbert", "Orson Scott Card", 
"Douglas Adams", "H. G. Wells", "Leigh Brackett"]

# Sorting by last name straigthforward way
# def get_last_name(s):
#     return s.split(' ')[-1].lower()

# scifi_authors.sort(key = get_last_name)
# print(scifi_authors)

# Sorting by last name elegant way with a lambda-expression
scifi_authors.sort(key = lambda name: name.split(' ')[-1].lower())
print(scifi_authors)

# Function that returns functions
def build_quadratic(a,b,c):
    """Returns a qudratic function f(x) = a*x^2 + bx + c"""
    return lambda x: a*x**2 + b*x + c

f = build_quadratic(3,2,1)  # f(x) = 3*x^2 + 2x + 1
print(f(2))
