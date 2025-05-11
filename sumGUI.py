import tkinter as tk
def conca():
    str1 = (stre1.get())
    str2 = (stre2.get())
    res = str1 + str2
    labres.config((res))
t = tk.Tk()
t.title("concatinationnnn")
t.geometry("600x600")

tk.Label(t,text="Enter NUMBER 1 ").pack()
stre1 = tk.Entry(t)
stre1.pack()
tk.Label(t,text="Enter NUMBER 2 ").pack()
stre2 = tk.Entry(t)
stre2.pack()
tk.Button(t,text="ivide njekkuu",command=conca).pack()
labres = tk.Label(t,text="result ===")
labres.pack()

t.mainloop()
    