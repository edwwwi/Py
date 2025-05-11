import matplotlib.pyplot as plt

# Data for two lines
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]     # Line 1
y2 = [1, 4, 9, 16, 25]    # Line 2

# Plot both lines
plt.plot(x, y1, label='Linear', color='blue')   # Line 1
plt.plot(x, y2, label='Quadratic', color='green') # Line 2

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Two Line Plot Example')

# Show legend
plt.legend()

# Show plot
plt.show()
