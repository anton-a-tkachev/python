# Random walk Monte-Carlo Simulation
import random

# def random_walk(n):
#     """Returns coordinates after 'n' random walks"""
#     x = 0
#     y = 0
#     for i in range(n):
#         step = random.choice(['N', 'S', 'E', 'W'])
#         if   step == 'E': x += 1
#         elif step == 'N': y += 1
#         elif step == 'S': y -= 1
#         else            : x -= 1
#     return (x, y)

# for i in range(25):
#     walk = random_walk(10)
#     print(walk, "Distance from home =", abs(walk[0]) + abs(walk[1]))

def random_walk(n):
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (1, 0), (-1, 0), (0, -1)])
        x += dx
        y += dy
    return (x, y)

number_of_walks = 20000
for walk_length in range(1,31):
    no_transport = 0
    for i in range(number_of_walks):
        (x, y) = random_walk(walk_length)
        distance = abs(x) + abs(y)
        if distance < 5: no_transport += 1

    no_transport_percentage = no_transport/number_of_walks
    print("Walk length =", walk_length, "% of no transport =", 100*no_transport_percentage)
