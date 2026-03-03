import tkinter as tk
from tkinter import ttk

class ChooseNumberPage(tk.Frame):
	def __init__(self, parent, app):
		super().__init__(parent)

		self.textLabel = ttk.Label(self, text="THIS IS WHERE THE NUMBER CHOICE HAPPENS")
		self.textLabel.place(relx=0.5, rely=0.5, anchor="center")

		self.numbersLabelText = tk.StringVar()
		self.numbersLabelText.set(f"current numbers: {app.game.random_numbers_choice}")
		self.numbersLabel = ttk.Label(self, textvariable=self.numbersLabelText)
		self.numbersLabel.place(relx=0.5, rely=0.6, anchor="center")

		self.chooseBtn = ttk.Button(self, text="CHOOSE NUMBER", command=lambda: app.show_page("GamePage"))
		self.chooseBtn.place(relx=0.5, rely=0.7, anchor="center")

		self.buttonFrame = ttk.Frame()
		self.buttonFrame.place(relx=0.5, rely=0.8, anchor="center")

		self.backBtn = ttk.Button(
			self,
			text="BACK",
			command=lambda: app.show_page("MainMenuPage")
		)
		self.backBtn.place(relx=0.5, rely=0.9, anchor="center")
	
	def refresh(self, app):
		self.numbersLabelText.set(f"current numbers: {app.game.random_numbers_choice}")