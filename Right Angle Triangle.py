a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
    print("It is a right triangle.")
else:
    print("It is NOT a right triangle.")