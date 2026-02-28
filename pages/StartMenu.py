import tkinter as tk
from tkinter import ttk

class StartMenu(tk.Frame):
	def __init__(self, parent, app):
		super().__init__(parent)
		
		self.startBtnImg = tk.PhotoImage(file = "assets\images\startBtn.png")
		
		playLabel = tk.Label(self, image=self.startBtnImg, borderwidth=0, highlightthickness=0)
		playLabel.bind("<Button-1>", lambda event: app.show_page("RandomizerPage"))
		playLabel.place(relx=0.5, rely=0.8, anchor="center")

		close_button = ttk.Button(app, text='X', command=app.destroy)
		close_button.pack(side="top")