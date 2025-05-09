n = int(input("Enter how many numbers: "))
even = 0
odd = 0

for i in range(n):
    num = int(input("Enter number: "))
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:",even)
print("Odd numbers:",odd)