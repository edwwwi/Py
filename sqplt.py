import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 =[1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]
y3 = [2, 4, 6, 8, 10] 

# Plotting the lines
plt.plot(x, y1, label='y = x^2', color='blue', marker='o')
plt.plot(x, y2, label='y = x', color='green', marker='s')
plt.plot(x, y3, label='y = x', color='red', marker='*')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Multiple Lines on Same Plot')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()

# First line
# Second line