import tkinter as tk

# Conversion rates
INR_TO_EUR = 0.011
EUR_TO_INR = 1 / INR_TO_EUR  # Approx 90.91

def convert_to_eur():
    inr = float(entry_inr.get())
    eur = round(inr * INR_TO_EUR, 4)
    entry_eur.delete(0, tk.END)
    entry_eur.insert(0, str(eur))

def convert_to_inr():
    eur = float(entry_eur.get())
    inr = round(eur * EUR_TO_INR, 2)
    entry_inr.delete(0, tk.END)
    entry_inr.insert(0, str(inr))

# GUI Setup
root = tk.Tk()
root.title("Currency Converter")

# Labels
tk.Label(root, text="INR:").grid(row=0, column=0)
tk.Label(root, text="EUR:").grid(row=1, column=0)

# Entry fields
entry_inr = tk.Entry(root)
entry_eur = tk.Entry(root)
entry_inr.grid(row=0, column=1)
entry_eur.grid(row=1, column=1)

# Buttons
btn_inr_to_eur = tk.Button(root, text="INR ➜ EUR", command=convert_to_eur)
btn_eur_to_inr = tk.Button(root, text="EUR ➜ INR", command=convert_to_inr)
btn_inr_to_eur.grid(row=2, column=0)
btn_eur_to_inr.grid(row=2, column=1)

root.mainloop()
