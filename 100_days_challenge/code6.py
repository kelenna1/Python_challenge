#Calculator with GUI
import tkinter as tk 

def press(button_text):
    entry_var.set(entry_var.get() + button_text)

def evaluate():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except Exception:
        entry_var.set("Error")

def clear():
    entry_var.set("")


root = tk.Tk()
root.title("calculator")
root.geometry("400x600")


entry_var = tk.StringVar

entry = tk.Entry(root, textvariable= entry_var, font = ('Arial', 24), bd = 10, insertwidth = 4, width = 14, borderwidth = 4)
entry.grid(row=0,column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button()