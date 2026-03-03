import tkinter as tk
from tkinter import ttk

class MainMenuPage(tk.Frame):
	def __init__(self, parent, app):
		super().__init__(parent)
		
		startBtn = ttk.Button(self, text='PLAY', command=lambda: app.new_round())
		startBtn.place(relx=0.5, rely=0.5, anchor="center")

		infoBtn = ttk.Button(self, text='INFO', command=lambda: app.show_page("InfoPage"))
		infoBtn.place(relx=0.5, rely=0.6, anchor="center")

		close_button = ttk.Button(self, text='EXIT', command=app.destroy)
		close_button.place(relx=0.5, rely=0.9, anchor="center")