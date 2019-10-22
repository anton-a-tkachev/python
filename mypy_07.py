# Lists

# example = list()
# example = []

primes = [2,3,5,7,11,13]    # create a list
print(primes)
primes.append(17)           # append a value
primes.append(19)           # append a value
print(primes)
print(primes[0])            # get element from the beginning
print(primes[-1])           # get element from the end
print(primes[-8])           # get element from the end
print(primes[2:5])          # slicing, primes[5] is excluded
print(primes[0:6])
print()

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
print(numbers + letters)
print(letters + numbers)