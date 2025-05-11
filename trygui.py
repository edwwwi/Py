import tkinter as tk
def area():
    length = float(entry_length.get())
    bredth = float(entry_breadth.get())
    result = length * bredth
    labelres.config(text="Area: " +str(result))
t = tk.Tk()
t.title("Area")
ent_length = tk.Label(t,text="Enter Length")
ent_length.pack()
entry_length=tk.Entry(t)
entry_length.pack()
ent_breadth = tk.Label(t,text="Enter Breadth")
ent_breadth.pack()
entry_breadth=tk.Entry(t)
entry_breadth.pack()

butt = tk.Button(t,text="Calc AREA",command=area)
butt.pack()
labelres = tk.Label(t,text = "AREA ")
labelres.pack()
t.mainloop()