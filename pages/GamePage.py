import tkinter as tk
from tkinter import ttk

class GamePage(tk.Frame):
	def __init__(self, parent, app):
		super().__init__(parent)

		pointsFrame = tk.Frame(self, bd=3, relief="ridge")
		pointsFrame.place(relx=0.5, rely=0.1, anchor="center")
		self.playerScore = tk.StringVar()
		playerScoreLabel = ttk.Label(
			pointsFrame,
			textvariable=self.playerScore,
			font=("Arial", 15)
		)
		playerScoreLabel.pack(padx=10, pady=10)

		currentNumberFrame = tk.Frame(self, bd=5, relief="raised")
		currentNumberFrame.place(relx=0.5, rely=0.5, anchor="center")
		self.currentNumberText = tk.IntVar()
		currentNumberLabel = ttk.Label(
			currentNumberFrame,
			textvariable=self.currentNumberText,
			font=("Arial", 40)
		)
		currentNumberLabel.pack(padx=50, pady=20)

		backBtn = ttk.Button(self, text="BACK (to main menu)", command=lambda: app.show_page("MainMenuPage"))
		backBtn.place(relx=0.5, rely=0.9, anchor="center")
	
	def refresh(self, app):
		self.currentNumberText.set(app.game.current_number)
		self.playerScore.set("Spēlētāja punkti: " + str(app.game.player_score))