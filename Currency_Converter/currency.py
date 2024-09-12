import tkinter as tk

# Hard-coded exchange rate
USD_TO_INR_RATE = 82.75  # Example rate, 1 USD = 82.75 INR
INR_TO_USD_RATE = 1 / USD_TO_INR_RATE

# Functions for conversion
def convert_currency():
    try:
        amount = float(amount_entry.get())
        if from_currency.get() == "USD" and to_currency.get() == "INR":
            converted_amount = amount * USD_TO_INR_RATE
            result.set(f"{converted_amount:.2f} INR")
        elif from_currency.get() == "INR" and to_currency.get() == "USD":
            converted_amount = amount * INR_TO_USD_RATE
            result.set(f"{converted_amount:.2f} USD")
        else:
            result.set("Select valid currencies")
    except ValueError:
        result.set("Enter a valid amount")

# Create the main window
root = tk.Tk()
root.title("Currency Converter")

# Create StringVars to hold user inputs and results
amount = tk.StringVar()
from_currency = tk.StringVar(value="USD")
to_currency = tk.StringVar(value="INR")
result = tk.StringVar()

# Create widgets
amount_entry = tk.Entry(root, textvariable=amount)
amount_entry.grid(row=0, column=1, padx=10, pady=5)

from_currency_menu = tk.OptionMenu(root, from_currency, "USD", "INR")
from_currency_menu.grid(row=1, column=1, padx=10, pady=5)

to_currency_menu = tk.OptionMenu(root, to_currency, "USD", "INR")
to_currency_menu.grid(row=2, column=1, padx=10, pady=5)

convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=1, padx=10, pady=5)

result_label = tk.Label(root, textvariable=result)
result_label.grid(row=4, column=1, padx=10, pady=5)

# Create labels
amount_label = tk.Label(root, text="Amount:")
amount_label.grid(row=0, column=0, padx=10, pady=5)

from_currency_label = tk.Label(root, text="From Currency:")
from_currency_label.grid(row=1, column=0, padx=10, pady=5)

to_currency_label = tk.Label(root, text="To Currency:")
to_currency_label.grid(row=2, column=0, padx=10, pady=5)

# Start the main event loop
root.mainloop()
