# Recursion

# Explicit memorization
fibonacci_cache = {}    # a dictionary

def fibonacci(n):
    # If the n-th value is found in cache then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n <= 2:
        value = 1
    else:
        value = fibonacci(n-1) + fibonacci(n-2)

    fibonacci_cache[n] = value
    return value

# Implicit memorization
from functools import lru_cache

@lru_cache()
def fibonacci1(n):
    if type(n) != int:
        raise TypeError("n must be a positive integer")
    if n < 1:
        raise ValueError("n must be a positive integer")

    if n < 3:
        return 1
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)

for n in range(1, 101):
    print(n,":",fibonacci1(n))
