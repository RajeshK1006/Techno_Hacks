import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Simulator")
        self.balance = 0  # Initial balance
        
        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Balance label
        self.balance_label = tk.Label(self.root, text="Balance: $0.00", font=('Arial', 14))
        self.balance_label.pack(pady=10)
        
        # Deposit
        self.deposit_frame = tk.Frame(self.root)
        self.deposit_frame.pack(pady=5)
        
        self.deposit_label = tk.Label(self.deposit_frame, text="Deposit Amount:")
        self.deposit_label.pack(side=tk.LEFT)
        
        self.deposit_amount = tk.Entry(self.deposit_frame)
        self.deposit_amount.pack(side=tk.LEFT)
        
        self.deposit_button = tk.Button(self.deposit_frame, text="Deposit", command=self.deposit)
        self.deposit_button.pack(side=tk.LEFT, padx=5)
        
        # Withdraw
        self.withdraw_frame = tk.Frame(self.root)
        self.withdraw_frame.pack(pady=5)
        
        self.withdraw_label = tk.Label(self.withdraw_frame, text="Withdraw Amount:")
        self.withdraw_label.pack(side=tk.LEFT)
        
        self.withdraw_amount = tk.Entry(self.withdraw_frame)
        self.withdraw_amount.pack(side=tk.LEFT)
        
        self.withdraw_button = tk.Button(self.withdraw_frame, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack(side=tk.LEFT, padx=5)
        
        # Check Balance
        self.check_balance_button = tk.Button(self.root, text="Check Balance", command=self.check_balance)
        self.check_balance_button.pack(pady=10)

    def deposit(self):
        try:
            amount = float(self.deposit_amount.get())
            if amount > 0:
                self.balance += amount
                self.deposit_amount.delete(0, tk.END)
                self.update_balance()
            else:
                messagebox.showwarning("Invalid Amount", "Deposit amount must be positive.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def withdraw(self):
        try:
            amount = float(self.withdraw_amount.get())
            if amount > 0:
                if amount <= self.balance:
                    self.balance -= amount
                    self.withdraw_amount.delete(0, tk.END)
                    self.update_balance()
                else:
                    messagebox.showwarning("Insufficient Funds", "You do not have enough balance to withdraw.")
            else:
                messagebox.showwarning("Invalid Amount", "Withdrawal amount must be positive.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def check_balance(self):
        self.update_balance()
        messagebox.showinfo("Balance", f"Your current balance is: ${self.balance:.2f}")

    def update_balance(self):
        self.balance_label.config(text=f"Balance: ${self.balance:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ATM(root)
    root.mainloop()
