import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.board = [None] * 9
        self.current_player = 'X'

        self.buttons = [tk.Button(root, text="", font=('Arial', 20), width=5, height=2,
                                 command=lambda i=i: self.on_button_click(i)) for i in range(9)]

        for i, button in enumerate(self.buttons):
            button.grid(row=i // 3, column=i % 3)

        self.restart_button = tk.Button(root, text="Restart", command=self.restart_game)
        self.restart_button.grid(row=3, column=0, columnspan=3)

        self.is_ai_mode = False

    def on_button_click(self, index):
        if self.board[index] is None and not self.check_winner() and not self.check_draw():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                if self.is_ai_mode and self.current_player == 'O':
                    self.ai_move()

    def ai_move(self):
        available_moves = [i for i, x in enumerate(self.board) if x is None]
        if available_moves:
            move = random.choice(available_moves)
            self.on_button_click(move)

    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]

        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] is not None:
                return True
        return False

    def check_draw(self):
        return all(x is not None for x in self.board)

    def restart_game(self):
        for button in self.buttons:
            button.config(text="")
        self.board = [None] * 9
        self.current_player = 'X'
        self.is_ai_mode = messagebox.askyesno("Play against AI", "Do you want to play against AI?")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
