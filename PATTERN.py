n = int(input("Enter the row size for the pattern: "))
for i in range(1, n + 1):  # Outer loop for rows
    for j in range(n  - i):  # Inner loop for spaces
        print(" ", end=" ")
    for k in range(1, 2 * i):  # Inner loop for stars
        print("*", end=" ")
    print()