import tkinter as tk
from tkinter import ttk


class CanvasButton:
	_counter = 0

	def __init__(
		self,
		canvas,
		x,
		y,
		image_normal,
		image_hover,
		image_pressed,
		command,
		text=None,
		font=None,
		fill="white",
		fill_hover="white",
		anim_steps=4,
		anim_scale=0.92,
		anim_delay_ms=15,
	):
		CanvasButton._counter += 1
		self.tag = f"canvas_btn_{CanvasButton._counter}"
		self.canvas = canvas
		self.center = (x, y)
		self.image_normal = image_normal
		self.image_hover = image_hover
		self.image_pressed = image_pressed
		self.command = command
		self.text = text
		self.font = font
		self.fill = fill
		self.fill_hover = fill_hover
		self.anim_steps = anim_steps
		self.anim_scale = anim_scale
		self.anim_delay_ms = anim_delay_ms
		self.animating = False

		self.image_id = canvas.create_image(x, y, image=image_normal, tags=self.tag)
		self.text_id = None
		if text is not None:
			self.text_id = canvas.create_text(
				x,
				y,
				text=text,
				font=font,
				fill=fill,
				tags=self.tag,
			)

		canvas.tag_bind(self.tag, "<Enter>", self.on_enter)
		canvas.tag_bind(self.tag, "<Leave>", self.on_leave)
		canvas.tag_bind(self.tag, "<Button-1>", self.on_click)

	def set_position(self, x, y):
		x0, y0 = self.center
		dx = x - x0
		dy = y - y0
		if dx or dy:
			self.canvas.move(self.tag, dx, dy)
			self.center = (x, y)

	def on_enter(self, _event):
		if not self.animating:
			self.canvas.itemconfigure(self.image_id, image=self.image_hover)
			if self.text_id is not None:
				self.canvas.itemconfigure(self.text_id, fill=self.fill_hover)

	def on_leave(self, _event):
		if not self.animating:
			self.canvas.itemconfigure(self.image_id, image=self.image_normal)
			if self.text_id is not None:
				self.canvas.itemconfigure(self.text_id, fill=self.fill)

	def on_click(self, _event):
		if self.animating:
			return
		self.canvas.itemconfigure(self.image_id, image=self.image_pressed)
		self.animating = True
		self._animate_press(step=0, phase="down")

	def _animate_press(self, step, phase):
		cx, cy = self.center
		if phase == "down":
			factor = self.anim_scale ** (1 / self.anim_steps)
			self.canvas.scale(self.tag, cx, cy, factor, factor)
			if step + 1 < self.anim_steps:
				self.canvas.after(self.anim_delay_ms, lambda: self._animate_press(step + 1, "down"))
			else:
				self.canvas.after(self.anim_delay_ms, lambda: self._animate_press(0, "up"))
		else:
			factor = (1 / self.anim_scale) ** (1 / self.anim_steps)
			self.canvas.scale(self.tag, cx, cy, factor, factor)
			if step + 1 < self.anim_steps:
				self.canvas.after(self.anim_delay_ms, lambda: self._animate_press(step + 1, "up"))
			else:
				self.animating = False
				self.command()

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
		self.canvas = tk.Canvas(self, highlightthickness=0)
		self.canvas.pack(fill="both", expand=True)

		self.btn_img = tk.PhotoImage(file="assets/images/btn.png")
		self.btn_hover_img = tk.PhotoImage(file="assets/images/halfPressedbtn.png")
		self.btn_pressed_img = tk.PhotoImage(file="assets/images/pressedBtn.png")

		self.play_btn = CanvasButton(
			self.canvas,
			0,
			0,
			image_normal=self.btn_img,
			image_hover=self.btn_hover_img,
			image_pressed=self.btn_pressed_img,
			command=lambda: app.show_page("RandomizerPage"),
		)

		self.canvas.bind("<Configure>", self._on_resize)

	def _on_resize(self, event):
		self.play_btn.set_position(event.width * 0.5, event.height * 0.8)
		


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