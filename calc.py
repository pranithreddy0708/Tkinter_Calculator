import tkinter as tk
root = tk.Tk()
root.title("Calculator")
root.config(bg="lightgray")
root.resizable(True, True)
entry = tk.Entry(
    root,
    font=("segoe ui", 16),
    bg="dark grey",
    fg="white",
    bd=0,
    justify="right",
    
)
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10)
def press(v):
    entry.insert(tk.END, v)
def clear():
    entry.delete(0, tk.END)
def calculate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-", 
    ".", "0", "=", "+"
]
r=1
c=0
for b in buttons:
    cmd =calculate if b == "=" else lambda x=b: press(x)
    tk.Button(
        root,
        text=b,
        command=cmd,
        font=("segoe ui", 14),
        width=5,
        height=2,
        bg="red",
        fg="black",
        bd=0,
        cursor="hand2"
    ).grid(row=r, column=c, padx=5, pady=5)
    c+=1
    if c==4:
        c=0
        r+=1
tk.Button(
    root,
    text="C",
    command=clear,
    font=("segoe UI",14),
    bg="Red",
    fg="white",
    bd=0,
    width=22,
    height=2
).grid(row=r, column=c, columnspan=4, pady=8)
root.mainloop()