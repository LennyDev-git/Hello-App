import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("800x500")
root.title("Hello App")

def hello():
    name = entry.get()
    
    if name == "":
        messagebox.showerror("ERROR","Please enter a name")
        
    else:
        messagebox.showinfo("Hello",f"Hello {name} have a nice day!")
    
entry = tk.Entry(root)
entry.pack()

button = tk.Button(root,text="Say hello",command=hello)
button.pack()


root.mainloop()
