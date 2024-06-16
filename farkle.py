'''

Farkle Game:
Programming Language: Python
Interface: GUI based

'''

import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import random
from collections import OrderedDict
from operator import itemgetter

__version__ = '0.1.1'

TARGET_SCORE = 10000
POINTS = OrderedDict((
    ('111', 1000),
    ('666', 600),
    ('555', 500),
    ('444', 400),
    ('333', 300),
    ('222', 200),
    ('1', 100),
    ('5', 50),
))


def roll_dice(num):
    return ''.join(sorted(str(random.randint(1, 6)) for _ in range(num)))


class FarkleGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Farkle")
        self.master.geometry("600x800")
        self.players = []
        self.current_player_index = 0
        self.current_score = 0
        self.current_roll = ""
        self.chosen = False
        self.last_round = False

        self.create_widgets()

    def choose_combo(self):
        """Handle choosing a scoring combo."""
        selection = self.combos_listbox.curselection()
        if selection:
            index = selection[0]
            combos = [combo for combo in POINTS if combo in self.current_roll]
            combo = combos[index]
            self.current_roll = self.current_roll.replace(combo, '', 1)
            self.current_score += POINTS[combo]
            self.chosen = True
            self.update_status()
            self.update_combos_listbox()


    def create_widgets(self):
        """Create the main widgets for the game."""
        self.info_label = ttk.Label(self.master, text="Welcome to Farkle!", font=("Helvetica", 16))
        self.info_label.pack(pady=10)

        self.status_label = ttk.Label(self.master, text="", font=("Helvetica", 12))
        self.status_label.pack(pady=5)

        self.roll_button = ttk.Button(self.master, text="Roll Dice", command=self.roll_dice_action)
        self.roll_button.pack(pady=5)

        self.combos_listbox = tk.Listbox(self.master, height=10, width=50)
        self.combos_listbox.pack(pady=5)

        self.choose_button = ttk.Button(self.master, text="Choose Combo", command=self.choose_combo)
        self.choose_button.pack(pady=5)

        self.end_turn_button = ttk.Button(self.master, text="End Turn", command=self.end_turn)
        self.end_turn_button.pack(pady=5)

        self.players_label = ttk.Label(self.master, text="", font=("Helvetica", 12))
        self.players_label.pack(pady=10)

        self.start_game()

    def start_game(self):
        """Initialize the game with player inputs."""
        human_players = self.input_to_int("Enter number of human players: ")
        ai_players = self.input_to_int("Enter number of AI players: ")
        if not human_players and not ai_players:
            return

        names = ['Mary AI', 'Bob AI', 'Ben AI', 'Eryn AI', 'John AI', 'Ellen AI', 'Elizabeth AI', 'Jason AI']
        random.shuffle(names)

        for num in range(1, human_players + 1):
            name = self.input_text(f"Player {num} enter your name: ")
            self.players.append({'ai': False, 'score': 0, 'name': name, 'done': False})
        for num in range(1, ai_players + 1):
            name = names[num - 1] if num <= len(names) else str(num)
            self.players.append({'ai': True, 'score': 0, 'name': name, 'done': False})

        self.update_status()
        self.update_players_label()

    def input_to_int(self, message):
        """Get an integer input fromthe user."""
        while True:
            try:
                player_num = int(self.input_text(message))
                if 0 <= player_num < 100:
                    return player_num
                else:
                    messagebox.showerror("Input Error", "Input must be between 0 and 99.")
            except ValueError:
                messagebox.showerror("Input Error", "Invalid input. Please enter a number.")
    
    def input_text(self, message):
        """Get a string input from the user."""
        return simpledialog.askstring("Input", message)

    def update_status(self):
        """Update the status label with the current player's information."""
        print("Current Score:", self.current_score)  # Debug print
        print("Player Score:", self.players[self.current_player_index]['score'])  # Debug print

        if self.current_roll:
            roll_text = self.current_roll if self.current_roll else 'Hot dice!'
        else:
            roll_text = 'Click "Roll Dice" to start!'
        player = self.players[self.current_player_index]
        self.status_label.config(
            text=f"{player['name']} has score {self.current_score} and {player['score']} banked. Dice: {roll_text}"
        )


    def update_players_label(self):
        """Update the label displaying the players' scores."""
        status = "="*13 + " Status " + "="*14 + "\n"
        for player in self.players:
            status += f"{player['name']} has {player['score']} points.\n"
        self.players_label.config(text=status)

    def roll_dice_action(self):
        """Roll the dice and update the status."""
        self.current_roll = roll_dice(6 if not self.current_roll else len(self.current_roll))
        self.chosen = False
        self.update_status()
        self.update_combos_listbox()

    def update_combos_listbox(self):
        """Update the listbox with valid scoring combinations."""
        self.combos_listbox.delete(0, tk.END)
        combos = [combo for combo in POINTS if combo in self.current_roll]
        for idx, c in enumerate(combos, 1):
            self.combos_listbox.insert(tk.END, f"({idx}) Remove {c} for {POINTS[c]} points.")
        if not combos:
            messagebox.showinfo("Farkle", "FARKLED!")
            self.current_score = 0  # Reset score to 0 on Farkle
            self.end_turn()  # End the turn after Farkle

    def end_turn(self):
        """End the current player's turn."""
        self.players[self.current_player_index]['score'] += self.current_score
        self.current_score = 0  # Reset current score to 0 at the end of turn
        self.current_roll = ""  # Reset current roll
        self.chosen = False
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        if self.players[self.current_player_index]['score'] >= TARGET_SCORE:
            self.players[self.current_player_index]['done'] = True
            self.last_round = True
        self.update_status()  # Update status after ending turn
        self.update_players_label()
        if all(player['done'] for player in self.players):
            self.end_game()

    def end_game(self):
        """End the game and determine the winner."""
        max_score = max(self.players, key=itemgetter('score'))['score']
        winners = [pl for pl in self.players if pl['score'] == max_score]
        winner_names = ', '.join([winner['name'] for winner in winners])
        messagebox.showinfo("Game Over", f"{winner_names} is the winner with {max_score} points.")
        self.master.quit()

if __name__ == '__main__':
    root = tk.Tk()
    game = FarkleGame(root)
    root.mainloop()
