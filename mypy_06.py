# Sets
ex = set()

# Add data
ex.add(42)
ex.add(False)
ex.add(3.141592)
ex.add("Thorium")

ex.add(42)      # Trying to add a duplicate
print(ex)
print("Set length is",len(ex),'\n')

ex.remove(42)   # Removing an element
print(ex)
print("Set length is",len(ex),'\n')

ex.discard(50)  # Discard an element
print(ex)
print("Set length is",len(ex),'\n')

ex2 = set([28, True, 2.71828, "Helium"])
print(ex2)
print("Set length is",len(ex2),'\n')

ex2.clear()
print(ex2)
print("Set length is",len(ex2),'\n')

odds = set([1,3,5,7,9])     # odd numbers between 1 and 10
evns = set([2,4,6,8,10])    # even numbers
prms = set([2,3,5,7])       # prime numbers
cmps = set([4,6,8,9,10])    # composite numbers

print("Union of odds and evens",set.union(odds,evns))
print("Union of primes and composites",set.union(prms,cmps))
print("Intersection of odds and primes",set.intersection(odds,prms))
print("Intersection of evens and primes",set.intersection(evns,prms))
print("Intersection of evens and odds",set.intersection(evns,odds),'\n')

print("Is 2 in primes?\t\t",2 in prms)
print("Is 6 in odds?\t\t",6 in odds)
print("Is 9 not in evens?\t",9 not in evns)