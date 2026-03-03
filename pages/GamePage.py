import tkinter as tk
from tkinter import ttk

class GamePage(tk.Frame):
	def __init__(self, parent, app):
		super().__init__(parent)

		currentNumberFrame = tk.Frame(self, bd=5, relief="raised")
		currentNumberFrame.place(relx=0.5, rely=0.2, anchor="center")
		self.currentNumberText = tk.IntVar()
		currentNumberLabel = ttk.Label(
			currentNumberFrame,
			textvariable=self.currentNumberText,
			font=("Arial", 40)
		)
		currentNumberLabel.pack(padx=50, pady=20)

		textLabel = ttk.Label(self, text="THIS IS WHERE GAME HAPPENS")
		textLabel.place(relx=0.5, rely=0.5, anchor="center")

		backBtn = ttk.Button(self, text="BACK (to main menu)", command=lambda: app.show_page("MainMenuPage"))
		backBtn.place(relx=0.5, rely=0.9, anchor="center")
	
	def refresh(self, app):
		self.currentNumberText.set(app.game.current_number)