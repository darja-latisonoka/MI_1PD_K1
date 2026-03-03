import tkinter as tk
from tkinter import ttk

class MainMenuPage(tk.Frame):
	def __init__(self, parent, app):
		super().__init__(parent)

		title_art = r"""
		 ____  _       _     _             _   _ _ _             
		|  _ \(_)_   _(_) __| | ___ _ __  | | | | | |_ _ __ __ _ 
		| | | | \ \ / / |/ _` |/ _ \ '__| | | | | | __| '__/ _` |
		| |_| | |\ V /| | (_| |  __/ |    | |_| | | |_| | | (_| |
		|____/|_| \_/ |_|\__,_|\___|_|     \___/|_|\__|_|  \__,_|
		"""
		title_label = tk.Label(
			self,
			text=title_art,
			font=("Courier New", 12), # monospace fonts
			justify="center",
			anchor="n"
		)
		title_label.place(relx=0.41, rely=0.2, anchor="center")
		
		# play poga
		startBtn = ttk.Button(self, text='PLAY', command=lambda: app.start_new_round())
		startBtn.place(relx=0.5, rely=0.5, anchor="center")

		# info poga
		infoBtn = ttk.Button(self, text='INFO', command=lambda: app.show_page("InfoPage"))
		infoBtn.place(relx=0.5, rely=0.6, anchor="center")

		# exit poga
		close_button = ttk.Button(self, text='EXIT', command=app.destroy)
		close_button.place(relx=0.5, rely=0.9, anchor="center")

		# sākuma gājiena izvēle
		turnChoiceFrame = ttk.Frame(self, borderwidth=5, relief="raised")
		turnChoiceFrame.pack(side="bottom", anchor="sw", padx=20, pady=20)
		self.turnLabelText = tk.StringVar()
		self.turnLabelText.set("Starting turn: " + app.game.turn)
		turnLabel = ttk.Label(turnChoiceFrame, textvariable=self.turnLabelText)
		turnLabel.pack(padx=10, pady=10, anchor="w")
		turnSwitchBtn = ttk.Button(turnChoiceFrame, text="Switch!", command=lambda:self.switch_starting_turn(app))
		turnSwitchBtn.pack(padx=40, pady=10)

		# algoritma izvēle
		algoChoiceFrame = ttk.Frame(self, borderwidth=5, relief="raised")
		algoChoiceFrame.place(relx=1.0, rely=1.0, anchor="se", x=-20, y=-20)
		self.algoLabelText = tk.StringVar()
		self.algoLabelText.set("Selected algorithm: " + app.game.algorithm)
		algoLabel = ttk.Label(algoChoiceFrame, textvariable=self.algoLabelText)
		algoLabel.pack(padx=10, pady=10, anchor="w")
		algoSwitchBtn = ttk.Button(algoChoiceFrame, text="Switch!", command=lambda:self.switch_algorithm(app))
		algoSwitchBtn.pack(padx=65, pady=10)

	def refresh(self, app):
		self.turnLabelText.set("Starting turn: " + app.game.turn)
		self.algoLabelText.set("Selected algorithm: " + app.game.algorithm)
		
	def switch_starting_turn(self, app):
		app.game.switch_turn()
		self.refresh(app)

	def switch_algorithm(self, app):
		app.game.switch_algorithm()
		self.refresh(app)