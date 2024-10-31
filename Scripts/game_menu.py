import tkinter as tk
import subprocess

# Define functions to start each game
def play_pong():
    subprocess.Popen(["python", "pong.py"])

def play_slots():
    subprocess.Popen(["python", "slots.py"])

def play_blackjack():
    subprocess.Popen(["python", "blackjack.py"])


def play_dot_game():
    subprocess.Popen(["python", "dot game.py"])

def play_snake():
    subprocess.Popen(["python", "snake.py"])

# Main menu UI
root = tk.Tk()
root.title("Game Menu")
root.geometry("300x400")

label = tk.Label(root, text="Choose a Game", font=("Arial", 18))
label.pack(pady=20)

# Game buttons
pong_button = tk.Button(root, text="Pong", command=play_pong)
pong_button.pack(pady=5)

slots_button = tk.Button(root, text="Slots", command=play_slots)
slots_button.pack(pady=5)

blackjack_button = tk.Button(root, text="Blackjack", command=play_blackjack)
blackjack_button.pack(pady=5)


dot_game_button = tk.Button(root, text="Dot Game", command=play_dot_game)
dot_game_button.pack(pady=5)

snake_button = tk.Button(root, text="Snake", command=play_snake)
snake_button.pack(pady=5)

root.mainloop()
