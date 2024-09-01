import tkinter as tk
import random

class PacmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pacman Game")
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.pacman_x = 200
        self.pacman_y = 200
        self.pacman_direction = "right"
        self.food_x = random.randint(10, 390)
        self.food_y = random.randint(10, 390)
        self.create_pacman()
        self.create_food()
        self.bind_keys()
        self.update_game()

    def create_pacman(self):
        self.pacman = self.canvas.create_oval(self.pacman_x-10, self.pacman_y-10, self.pacman_x+10, self.pacman_y+10, fill="yellow")

    def create_food(self):
        self.food = self.canvas.create_oval(self.food_x-5, self.food_y-5, self.food_x+5, self.food_y+5, fill="red")

    def bind_keys(self):
        self.root.bind("<Key>", self.move_pacman)

    def move_pacman(self, event):
        if event.keysym == "Up":
            self.pacman_y -= 5
            self.canvas.move(self.pacman, 0, -5)
        elif event.keysym == "Down":
            self.pacman_y += 5
            self.canvas.move(self.pacman, 0, 5)
        elif event.keysym == "Left":
            self.pacman_x -= 5
            self.canvas.move(self.pacman, -5, 0)
        elif event.keysym == "Right":
            self.pacman_x += 5
            self.canvas.move(self.pacman, 5, 0)

    def update_game(self):
        if self.pacman_x-10 <= self.food_x <= self.pacman_x+10 and self.pacman_y-10 <= self.food_y <= self.pacman_y+10:
            self.canvas.delete(self.food)
            self.food_x = random.randint(10, 390)
            self.food_y = random.randint(10, 390)
            self.create_food()
        self.root.after(100, self.update_game)

if __name__ == "__main__":
    root = tk.Tk()
    game = PacmanGame(root)
    root.mainloop()