import tkinter as tk
from tkinter import messagebox
from updater import check_and_update

CURRENT_VERSION = "1.0"

def on_button_click(value):
    entry.insert(tk.END, value)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

def check_for_updates():
    messagebox.showinfo("Update Check", "Checking for updates...")
    check_and_update(CURRENT_VERSION)

root = tk.Tk()
root.title("Calculator")
root.geometry("325x425")
root.configure(bg="dark slate gray")

entry = tk.Entry(root, width=20, font=("Arial", 20), justify='right', bg="#F0F0F0")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]
for (text, row, col) in buttons:
    action = lambda x=text: on_button_click(x) if x != '=' else calculate()
    tk.Button(root, text=text, command=action, width=5, height=2, font=("Arial", 14), bg="slate grey", fg="white", relief=tk.GROOVE).grid(row=row, column=col, padx=5, pady=5)

tk.Button(root, text="C", command=clear, width=5, height=2, font=("Arial", 14), bg="red", fg="white", relief=tk.GROOVE).grid(row=5, column=0, padx=5, pady=5)
tk.Button(root, text="Update", command=check_for_updates, width=10, height=2, font=("Arial", 14), bg="green", fg="white", relief=tk.GROOVE).grid(row=5, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()
