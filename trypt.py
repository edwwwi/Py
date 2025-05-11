import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 =[1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]
y3 = [1, 20, 17,9 , 10]         # Cubic
y4 = [1.00, 1.41, 1.73, 2.00, 2.24] # Square Root
y5 = [2, 4, 8, 16, 32]           # Exponential

plt.plot(x,y1,label="sq",color='red')
plt.plot(x,y2,label="x",color='green')
plt.plot(x,y3,label="cub",color='cyan')
plt.plot(x,y4,label="sqr",color='blue')
plt.plot(x,y5,label="expo",color='yellow')

plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("TRY")
plt.legend()

plt.grid(True)
plt.show()