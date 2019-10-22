# Prime numbers
import time
import math

primes = [2]
def is_prime(num):
    """Returns True if the number is prime, False otherwise"""
    if type(num) != int: return False
    if num < 2: return False
    if num in primes: return True
    maxdiv = math.floor(math.sqrt(num))
    for div in primes:
        if num % div == 0: return False
        if div > maxdiv: break
    primes.append(num)
    return True

def get_prime(n):
    if type(n) != int: return 0
    if n < 1: return 0
    try:
        return primes[n-1]
    except:
        testnum = primes[len(primes) - 1] + 1
        while True:
            if is_prime(testnum):
                if len(primes) == n: return primes[-1]
            testnum += 1

# n = 10000
# t0 = time.time()
# my_prime = get_prime(n)
# t1 = time.time()
# print("Prime",n,':',my_prime)
# print("Time required:", t1 - t0)

t0 = time.time()
for n in range(1, 1000):
    if is_prime(n): print(n)
t1 = time.time()
print("Time required:", t1 - t0)

# print(primes)
