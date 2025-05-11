import numpy as np

# Single random integer from 0 to 99
x1 = np.random.randint(100)
print(x1)  # Example Output: 64

# Array of 5 random integers (0 to 99)
x2 = np.random.randint(100, size=5)
print(x2)  # Example Output: [25 62 24 81 39]

# 2D Array of random integers (shape = 3x5, values 0 to 99)
x3 = np.random.randint(100, size=(3, 5))
print(x3)  
# Example Output:
# [[ 2 96 40 43 85]
#  [81 81  4 48 29]
#  [80 31  6 10 24]]

# Single random float between 0 and 1
x4 = np.random.rand()
print(x4)  # Example Output: 0.2733166576024767

# Array of 10 random floats between 0 and 1
x5 = np.random.rand(10)
print(x5)  
# Example Output: [0.82536563 0.46789636 0.28863107 0.83941914 0.24424812 
#                  0.25816291 0.72567413 0.80770073 0.32845661 0.34451507]

# 2D array of random floats (shape = 3x5)
x6 = np.random.rand(3, 5)
print(x6)  
# Example Output:
# [[0.16220086 0.80935717 0.97331357 0.60975199 0.48542906]
#  [0.68311884 0.27623475 0.73447814 0.29257476 0.27329666]
#  [0.62625815 0.00697790 0.21403868 0.49191027 0.41167090]]

# Random choice from list
x7 = np.random.choice([3, 5, 6, 7, 9, 2])
print(x7)  # Example Output: 3

# 2D array of random choices from list
x8 = np.random.choice([3, 5, 6, 7, 9, 2], size=(3, 5))
print(x8)
# Example Output:
# [[3 2 5 2 6]
#  [5 9 3 6 9]
#  [5 6 9 3 3]]
