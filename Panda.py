import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather.csv")



# 6. Create a bar plot to visualize temperature of each day

plt.bar(df["date"], df["temperature"], color='skyblue')
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature of Each Day")
plt.tight_layout()
plt.legend()
plt.show()