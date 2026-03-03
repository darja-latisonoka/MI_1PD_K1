import tkinter as tk
from tkinter import ttk

class InfoPage(tk.Frame):
	def __init__(self, parent, app):
		super().__init__(parent)

		textLabel = ttk.Label(self, text="THIS IS WHERE WE COULD WRITE SOME INFO ABOUT RULES AND STUFF")
		textLabel.place(relx=0.5, rely=0.5, anchor="center")

		backBtn = ttk.Button(self, text="BACK", command=lambda: app.show_page("MainMenuPage"))
		backBtn.place(relx=0.5, rely=0.9, anchor="center")