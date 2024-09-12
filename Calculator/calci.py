import tkinter as tk

# Functions for arithmetic operations
def add():
    result.set(float(entry1.get()) + float(entry2.get()))

def subtract():
    result.set(float(entry1.get()) - float(entry2.get()))

def multiply():
    result.set(float(entry1.get()) * float(entry2.get()))

def divide():
    try:
        result.set(float(entry1.get()) / float(entry2.get()))
    except ZeroDivisionError:
        result.set("Error")

# Create the main window
root = tk.Tk()
root.title("Basic Calculator")

# Create a StringVar to store the result
result = tk.StringVar()

# Create Entry widgets for user input
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

# Create Label widgets to show the entry titles
label1 = tk.Label(root, text="Enter number 1:")
label2 = tk.Label(root, text="Enter number 2:")
result_label = tk.Label(root, text="Result:")

# Create Buttons for arithmetic operations
add_button = tk.Button(root, text="Add", command=add)
subtract_button = tk.Button(root, text="Subtract", command=subtract)
multiply_button = tk.Button(root, text="Multiply", command=multiply)
divide_button = tk.Button(root, text="Divide", command=divide)

# Create a Label to display the result
result_display = tk.Label(root, textvariable=result)

# Layout using grid
label1.grid(row=0, column=0, padx=10, pady=5)
entry1.grid(row=0, column=1, padx=10, pady=5)
label2.grid(row=1, column=0, padx=10, pady=5)
entry2.grid(row=1, column=1, padx=10, pady=5)
add_button.grid(row=2, column=0, padx=10, pady=5)
subtract_button.grid(row=2, column=1, padx=10, pady=5)
multiply_button.grid(row=3, column=0, padx=10, pady=5)
divide_button.grid(row=3, column=1, padx=10, pady=5)
result_label.grid(row=4, column=0, padx=10, pady=5)
result_display.grid(row=4, column=1, padx=10, pady=5)

# Run the application
root.mainloop()
