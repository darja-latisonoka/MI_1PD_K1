import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Divider Ultra")
		self.geometry("960x540")

		container = tk.Frame(self)
		container.pack(fill="both", expand=True)

		self.pages = {}
		for page_class in (StartMenu, RandomizerPage):
			page = page_class(container, self)
			self.pages[page_class.__name__] = page
			page.grid(row=0, column=0, sticky="nsew")

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.show_page("StartMenu")

	def show_page(self, page_name):
		self.pages[page_name].tkraise()


class StartMenu(tk.Frame):
	def __init__(self, parent, app):
		super().__init__(parent)
		
		self.startBtnImg = tk.PhotoImage(file = "assets\images\startBtn.png")
		
		playLabel = tk.Label(self, image=self.startBtnImg, borderwidth=0, highlightthickness=0)
		playLabel.bind("<Button-1>", lambda event: app.show_page("RandomizerPage"))
		playLabel.place(relx=0.5, rely=0.8, anchor="center")
		


class RandomizerPage(tk.Frame):
	def __init__(self, parent, app):
		super().__init__(parent)

		backBtn = ttk.Button(
			self,
			text="BACK",
			command=lambda: app.show_page("StartMenu")
		)
		backBtn.place(relx=0.5, rely=0.5, anchor="center")


if __name__ == "__main__":
	app = App()
	app.mainloop()