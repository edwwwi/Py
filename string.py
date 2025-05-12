# Using remove()
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")  # Removes 'banana'
print("After remove():", thisset)

# Using discard()
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")  # Also removes 'banana'
print("After discard():", thisset)

# Using pop()
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()  # Removes a random element
print("Popped element:", x)
print("After pop():", thisset)
