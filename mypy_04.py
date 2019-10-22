# If Then Else

# mypass = input("Please enter a password: ")
# myconf = input("Please confirm: ")

# if mypass == myconf:
#     print("Passwords match")
# else:
#     print("Passwords do not match")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

# Check if that's a triangle
if a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and c + a > b:
    # Identify the type
    if a != b and b != c and a != c:
        print("Scalene triangle")
    elif a == b and b == c:
        print("Equilateral triangle")
    else:
        print("Isosceles triangle")
else:
    print("Not a triangle")