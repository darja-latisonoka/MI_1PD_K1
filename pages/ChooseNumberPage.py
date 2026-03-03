import tkinter as tk
from tkinter import ttk

class ChooseNumberPage(tk.Frame):
	def __init__(self, parent, app):
		super().__init__(parent)

		textLabel = ttk.Label(self, text="THIS IS WHERE THE NUMBER CHOICE HAPPENS")
		textLabel.place(relx=0.5, rely=0.5, anchor="center")

		self.numbersLabelText = tk.StringVar()
		self.numbersLabelText.set(f"current numbers: {app.game.random_numbers_choice}")
		numbersLabel = ttk.Label(self, textvariable=self.numbersLabelText)
		numbersLabel.place(relx=0.5, rely=0.6, anchor="center")

		chooseBtn = ttk.Button(self, text="CHOOSE NUMBER", command=lambda: app.show_page("GamePage"))
		chooseBtn.place(relx=0.5, rely=0.7, anchor="center")

		buttonFrame = ttk.Frame()
		buttonFrame.place(relx=0.5, rely=0.8, anchor="center")

		backBtn = ttk.Button(self, text="BACK", command=lambda: app.show_page("MainMenuPage"))
		backBtn.place(relx=0.5, rely=0.9, anchor="center")
	
	def refresh(self, app):
		self.numbersLabelText.set(f"current numbers: {app.game.random_numbers_choice}")