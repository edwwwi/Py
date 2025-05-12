f = open("numbers.txt", "r")
numbers = []
for line in f:
    numbers.append(int(line.strip()))

f.close()

numbers.sort()

n = len(numbers)

if n % 2 == 1:
    median = numbers[n // 2]
else:
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

print("The median is:", median)