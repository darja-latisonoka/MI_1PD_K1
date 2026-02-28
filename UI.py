import tkinter as tk
from tkinter import ttk
import sv_ttk

from pages.StartMenu import *
from pages.RandomizerPage import *

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 540
PAGES = (StartMenu, RandomizerPage)

class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Divider Ultra")

		# open the app in the middle of the screen
		w = WINDOW_WIDTH
		h = WINDOW_HEIGHT
		screenW = self.winfo_screenwidth()
		screenH = self.winfo_screenheight()
		x = (screenW/2) - (w/2)
		y = (screenH/2) - (h/2)
		self.geometry('%dx%d+%d+%d' % (w, h, x, y))

		container = tk.Frame(self)
		container.pack(fill="both", expand=True)

		self.pages = {}
		for page_class in PAGES:
			page = page_class(container, self)
			self.pages[page_class.__name__] = page
			page.grid(row=0, column=0, sticky="nsew")

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.show_page("StartMenu")

	def show_page(self, page_name):
		self.pages[page_name].tkraise()

if __name__ == "__main__":
	app = App()
	sv_ttk.set_theme("dark")
	app.mainloop()