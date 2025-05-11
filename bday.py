import tkinter as tk
from datetime import datetime

def calculate_age():
    birth_year = int(entry_birth.get())
    current_year = datetime.now().year
    age = current_year - birth_year
    label_result.config(text="Age: " + str(age))

# GUI Setup
root = tk.Tk()
root.title("Age Calculator")

tk.Label(root, text="Enter Birth Year:").pack()
entry_birth = tk.Entry(root)
entry_birth.pack()

tk.Button(root, text="Calculate Age", command=calculate_age).pack()
label_result = tk.Label(root, text="Age: ")
label_result.pack()

root.mainloop()
