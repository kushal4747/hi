
import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry field
entry = tk.Entry(root, font="Arial 20", bd=10, relief=tk.RIDGE, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10)

# Button layout
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

for row in buttons:
    r = tk.Frame(button_frame)
    r.pack(expand=True, fill="both")
    for btn_text in row:
        btn = tk.Button(r, text=btn_text, font="Arial 18", relief=tk.RIDGE, bd=5)
        btn.pack(side=tk.LEFT, expand=True, fill="both")
        btn.bind("<Button-1>", click)

root.mainloop()
