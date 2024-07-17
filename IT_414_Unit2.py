import tkinter as tk
from tkinter import messagebox
def add_numbers(a, b):
    """Function that takes in two numbers and returns their sum."""
    return a + b
import tkinter as tk
from tkinter import messagebox

def main():
    """Function that sets up the GUI and calls the summing function."""
    def on_add_button_click():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            result = add_numbers(num1, num2)
            result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Input error", "Please enter valid numbers")
    
    root = tk.Tk()
    root.title("Add Two Numbers")

    tk.Label(root, text="Number 1:").grid(row=0, column=0)
    tk.Label(root, text="Number 2:").grid(row=1, column=0)
    
    entry1 = tk.Entry(root)
    entry1.grid(row=0, column=1)
    entry2 = tk.Entry(root)
    entry2.grid(row=1, column=1)
    
    add_button = tk.Button(root, text="Add", command=on_add_button_click)
    add_button.grid(row=2, column=0, columnspan=2)
    
    result_label = tk.Label(root, text="Result: ")
    result_label.grid(row=3, column=0, columnspan=2)
    
    root.mainloop()

if __name__ == "__main__":
    main()
