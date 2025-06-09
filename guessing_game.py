
import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Guess a number between 1 and 100", font=("Helvetica", 14)).pack(pady=20)

        self.entry = tk.Entry(self.root, font=("Helvetica", 12), justify='center')
        self.entry.pack(pady=10)

        self.feedback = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.feedback.pack(pady=10)

        self.submit_btn = tk.Button(self.root, text="Submit Guess", command=self.check_guess, font=("Helvetica", 12))
        self.submit_btn.pack(pady=10)

        self.reset_btn = tk.Button(self.root, text="Reset Game", command=self.reset_game, font=("Helvetica", 12))
        self.reset_btn.pack(pady=10)

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            self.feedback.config(text="Please enter a valid number.")
            return

        guess = int(guess)
        self.attempts += 1

        if guess < self.number_to_guess:
            self.feedback.config(text="Too low! Try again.")
        elif guess > self.number_to_guess:
            self.feedback.config(text="Too high! Try again.")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed it in {self.attempts} attempts!")
            self.feedback.config(text="You won!")
            self.submit_btn.config(state='disabled')

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.feedback.config(text="")
        self.submit_btn.config(state='normal')


if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGame(root)
    root.mainloop()
