import tkinter as tk


root = tk.Tk()
button = tk.Button(root, text="Click Me!", command=lambda: print("Button clicked!"))
button.pack()
root.mainloop()