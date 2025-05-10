
text = input("Enter a string: ")


count = {}

# Loop through each character in the string
for ch in text:
    # Count the character
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1


print("Character count:")
print(count)
