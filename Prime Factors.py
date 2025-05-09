n = int(input("Enter a number: "))
print("Prime factors:", end=" ")

i = 2
while i <= n:
    if n % i == 0:
        print(i, end=" ")
        n = n // i
    else:
        i += 1