def min_max0(numbers):
    smallest = numbers[0]
    largest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return smallest, largest

# Example usage
nums = [10, 2, 5, 8, 3]
min_val, max_val = min_max0(nums)
print("Smallest number:", min_val)
print("Largest number:", max_val)
