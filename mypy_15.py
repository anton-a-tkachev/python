# List comprehensions

# [expr for val in collection]
# [expr for val in collection if <condition>]
# [expr for val in collection if <condition_1> and <condition_2>]
# [expr for val_1 in collection_1 for val_2 in collection_2]

# squares = []
# for i in range(1,101):
#     squares.append(i**2)

# squares_2 = [i**2 for i in range(1,101)]

#print(squares)
#print(squares_2)

# remainders_5 = [i**2%5 for i in range(1,101)]
# print(remainders_5)

# remainders_11 = [i**2%11 for i in range(1,101)]
# print(remainders_11)

movies = [("Munich",2005),("The Prestige",2006),("The Departed",2006),
("Into the Wild",2007),("The Dark Knight",2008),("Mary and Max",2009),
("The King\'s Speech",2010),("The Help",2011),("The Artist",2011),
("Argo",2012),("12 Years a Slave",2013),("Birdman",2014),("Spotlight",2015),
("The BFG",2016)]

# tmovies = [title for title in movies if title.startswith('T')]
pre2010 = [title for (title, year) in movies if year < 2010]
print(pre2010)

# Cartesian product
A = [1,3,5,7]
B = [2,4,6,8]

cartesian_product = [(a, b) for a in A for b in B]
print("A =", A)
print("B =", B)
print("Cartesian product A x B =", cartesian_product)
