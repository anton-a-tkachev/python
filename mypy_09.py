# Tuples
import sys

primes = (2,3,5,7,11,13)
print(primes)
print(len(primes))
print()

for p in primes:
    print(p)

print()

tuple_ex = (1,2,3,4,5,6,7,8,9,10)
list_ex = [1,2,3,4,5,6,7,8,9,10]

print(sys.getsizeof(tuple_ex))
print(sys.getsizeof(list_ex))