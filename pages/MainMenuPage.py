import tkinter as tk
from tkinter import ttk

class MainMenuPage(tk.Frame):
	def __init__(self, parent, app):
		super().__init__(parent)
		
		self.startBtn = ttk.Button(self, text='Play', command=lambda: app.new_round())
		self.startBtn.place(relx=0.5, rely=0.5, anchor="center")

		self.infoBtn = ttk.Button(self, text='Info', command=lambda: app.show_page("InfoPage"))
		self.infoBtn.place(relx=0.5, rely=0.6, anchor="center")

		self.close_button = ttk.Button(self, text='Exit', command=app.destroy)
		self.close_button.place(relx=0.5, rely=0.9, anchor="center")