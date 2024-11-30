import tkinter as tk
import random

class PokemonGame(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Pokemon Game")
        self.geometry("400x400")

        self.player = PokemonPlayer()
        self.opponent = PokemonOpponent()

        self.label = tk.Label(self, text="Welcome to the Pokemon Game!")
        self.label.pack()

        self.button = tk.Button(self, text="Start Battle", command=self.start_battle)
        self.button.pack()

    def start_battle(self):
        self.label.config(text="")
        self.button.config(text="")

        self.player_label = tk.Label(self, text=f"Player: {self.player.name} - {self.player.pokemon.name} (HP: {self.player.pokemon.hp})")
        self.player_label.pack()

        self.opponent_label = tk.Label(self, text=f"Opponent: {self.opponent.name} - {self.opponent.pokemon.name} (HP: {self.opponent.pokemon.hp})")
        self.opponent_label.pack()

        self.button = tk.Button(self, text="Attack", command=self.attack)
        self.button.pack()

    def attack(self):
        damage = random.randint(1, 10)
        self.opponent.pokemon.hp -= damage

        self.player_label.config(text=f"Player: {self.player.name} - {self.player.pokemon.name} (HP: {self.player.pokemon.hp})")
        self.opponent_label.config(text=f"Opponent: {self.opponent.name} - {self.opponent.pokemon.name} (HP: {self.opponent.pokemon.hp})")

        if self.opponent.pokemon.hp <= 0:
            self.opponent.pokemon = None
            self.button.config(text="")
            self.label = tk.Label(self, text="You win!")
            self.label.pack()

class PokemonPlayer:
    def __init__(self):
        self.name = "Player"
        self.pokemon = Pokemon("Bulbasaur", 50)

class PokemonOpponent:
    def __init__(self):
        self.name = "Opponent"
        self.pokemon = Pokemon("Charmander", 50)

class Pokemon:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

if __name__ == "__main__":
    app = PokemonGame()
    app.mainloop()