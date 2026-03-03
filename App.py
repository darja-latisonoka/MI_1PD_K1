# MAIN ENTRY POINT
import tkinter as tk
import sv_ttk

from GameState import *

from pages.MainMenuPage import *
from pages.ChooseNumberPage import *
from pages.GamePage import *
from pages.InfoPage import *

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 540
PAGES = (MainMenuPage, ChooseNumberPage, GamePage, InfoPage)

class App(tk.Tk):
	def __init__(self):
		# iedarbina tk
		super().__init__()

		self.game = GameState()

		self.title("Divider Ultra")

		# atver aplikāciju ekrāna vidū
		w = WINDOW_WIDTH
		h = WINDOW_HEIGHT
		screenW = self.winfo_screenwidth()
		screenH = self.winfo_screenheight()
		x = (screenW/2) - (w/2)
		y = (screenH/2) - (h/2)
		self.geometry('%dx%d+%d+%d' % (w, h, x, y))

		# uztaisa frame, kur viss būs iekšā un uzliek to uz app
		container = tk.Frame(self)
		container.pack(fill="both", expand=True)

		# setapojam visu lapu objektus
		self.pages = {}
		for page_class in PAGES:
			page = page_class(container, self)        # lapai setto parent un iedodam arī app
			self.pages[page_class.__name__] = page    # ieliek lapu iekša dict objektā
			page.grid(row=0, column=0, sticky="nsew") # sastacko visas lapas vienu uz otras

		# liek lapām būt stretchable
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.show_page("MainMenuPage")
	
	# kad nospiež play sākas jauns raunds
	def new_round(self):
		self.game.new_round()	# updeito game state
		self.show_page("ChooseNumberPage")

	# parāda un updeito lapu
	def show_page(self, page_name):
		page = self.pages[page_name]
		page.tkraise()

		# ja ir refresh funkcija, tad refresho
		if hasattr(page, "refresh") and callable(page.refresh):
			page.refresh(self) # ar self iedod app

if __name__ == "__main__":
	app = App()
	sv_ttk.set_theme("dark")
	app.mainloop() # startē aplikāciju