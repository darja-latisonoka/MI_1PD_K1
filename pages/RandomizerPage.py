import tkinter as tk
from tkinter import ttk

class RandomizerPage(tk.Frame):
	def __init__(self, parent, app):
		super().__init__(parent)

		backBtn = ttk.Button(
			self,
			text="BACK",
			command=lambda: app.show_page("StartMenu")
		)
		backBtn.place(relx=0.5, rely=0.5, anchor="center")