d = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 1. len(d)
print("1. len(d) ➝", len(d))  # Total number of key-value pairs

# 2. aDict[key]
print("2. d['name'] ➝", d['name'])  # Access value using key

# 3. d.get(key [, default])
print("3. d.get('age') ➝", d.get('age'))  # Get value if key exists
print("   d.get('gender', 'Not Found') ➝", d.get('gender', 'Not Found'))  # Get default if key not found

# 4. d.pop(key [, default])
print("4. d.pop('city') ➝", d.pop('city'))  # Removes 'city'
print("   After pop, d ➝", d)

# 5. list(d.keys())
print("5. list(d.keys()) ➝", list(d.keys()))  # List of all keys

# 6. list(d.values())
print("6. list(d.values()) ➝", list(d.values()))  # List of all values

# 7. list(d.items())
print("7. list(d.items()) ➝", list(d.items()))  # List of (key, value) pairs

# 8. d.clear()
d.clear()
print("8. After d.clear(), d ➝", d)  # Now empty dictionary

# 9. for key in d:
d = {'x': 1, 'y': 2}
print("9. Looping through keys:")
for key in d:
    print(f"   Key: {key}, Value: {d[key]}")
