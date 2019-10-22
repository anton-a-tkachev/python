# Text files

# Straightforward approach
# f = open("machine_learning.txt")    # read mode by default
# text = f.read()
# f.close()

# print(text)

# Smart and safe technique
try:
    with open("machine_learning.txt") as f:
        text = f.read()
except FileNotFoundError:
    text = None

print(text)

# Writing to a text file
oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]

# with open("oceans.txt", 'w') as f:
#     for ocean in oceans:
#         f.write(ocean)
#         f.write('\n')

with open("oceans.txt", 'w') as f:
    [print(ocean, file = f) for ocean in oceans]

# Appending to a text file
with open("oceans.txt", 'a') as f:
    print("====================\nThese are the oceans", file = f)