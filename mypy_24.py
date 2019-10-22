# Recursion factorial
def fact(n: int):
    """Computes factorial of n"""
    assert n >= 0, "Factorial function undefined for negative numbers"
    if n == 0: return 1
    return n*fact(n-1)

print(fact(20))
