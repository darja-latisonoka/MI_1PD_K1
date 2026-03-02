import tkinter as tk
from tkinter import ttk

class StartMenuPage(tk.Frame):
	def __init__(self, parent, app):
		super().__init__(parent)
		
		startBtn = ttk.Button(self, text='Play', command=lambda: app.new_round())
		startBtn.place(relx=0.5, rely=0.5, anchor="center")

		close_button = ttk.Button(self, text='Exit', command=app.destroy)
		close_button.place(relx=0.5, rely=0.6, anchor="center")