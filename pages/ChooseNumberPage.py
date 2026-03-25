import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import ttk

BUTTON_COUNT = 5

class ChooseNumberPage(tk.Frame):
	def __init__(self, parent, app):
		super().__init__(parent)

		textLabel = ttk.Label(self, text="IZVĒLIES SKAITLI AR KURU SĀKT", font=("Arial", 20))
		textLabel.place(relx=0.5, rely=0.1, anchor="center")

		self.buttonFrame = tk.Frame(self, bd=5, relief="raised")
		self.buttonFrame.place(relx=0.5, rely=0.3, anchor="center")

		self.numberBtnTextList = [None] * BUTTON_COUNT
		for i in range(BUTTON_COUNT):
			self.numberBtnTextList[i] = tk.IntVar()
			button = ttk.Button(
				self.buttonFrame,
				textvariable=self.numberBtnTextList[i],
				command=lambda i=i: self.select_number(app, app.game.random_numbers_list[i])
			)
			button.pack(side="left", padx=20, pady=20)

		self.numbersLabelText = tk.StringVar()
		numbersLabel = ttk.Label(self, textvariable=self.numbersLabelText)
		numbersLabel.place(relx=0.5, rely=0.4, anchor="center")

		chooseBtn = ttk.Button(self, text="IZVĒLĒTIES (SĀKT SPĒLI)", command=lambda: self.choose_number(app))
		chooseBtn.place(relx=0.5, rely=0.5, anchor="center")

		backBtn = ttk.Button(self, text="ATPAKAĻ", command=lambda: app.show_page("MainMenuPage"))
		backBtn.place(relx=0.5, rely=0.9, anchor="center")
	
	def refresh(self, app):
		# atjaunot skaitļu pogas
		for i in range(BUTTON_COUNT):
			self.numberBtnTextList[i].set(app.game.random_numbers_list[i])

		# atjaunot šobrīdējā izvēlētā skaitļa label
		if app.game.selected_number == 0:
			self.numbersLabelText.set(f"Šobrīd izvēlētais skaitlis: NONE")
		else:
			self.numbersLabelText.set(f"Šobrīd izvēlētais skaitlis: {app.game.selected_number}")

	def select_number(self, app, number):
		app.game.select_number(number)
		self.refresh(app)
	
	def choose_number(self, app):
		n = app.game.selected_number
		if n == 0:
			msgbox.showwarning("Nav izvēlēts skaitlis", "Tev jāizvēlās kāds skaitlis, lai sāktu spēli!")
			return
		else:
			app.game.choose_number(app.game.selected_number)
		app.show_page("GamePage")