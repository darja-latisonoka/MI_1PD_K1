import tkinter as tk
from tkinter import ttk

class InfoPage(tk.Frame):
	def __init__(self, parent, app):
		super().__init__(parent)

		# Create a main frame with scrollbar
		mainFrame = ttk.Frame(self)
		mainFrame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

		# Title
		title = ttk.Label(mainFrame, text="SPĒLES NOTEIKUMI", font=("Helvetica", 16, "bold"))
		title.pack(pady=(0, 20))

		# Game Setup
		ttk.Label(mainFrame, text="SPĒLES SĀKUMS", font=("Helvetica", 12, "bold")).pack(anchor="w", pady=(10, 5))
		setup_text = ttk.Label(mainFrame, text="• Tiek ģenerēti 5 gadījuma skaitļi (1-5 miljoni, dalāmi ar 216)\n• Spēlētājs izvēlas sākuma skaitli\n• Gan cilvēks, gan AI sāk ar 0 punktiem\n• Spēles banka sāk ar 0 punktiem", justify=tk.LEFT, wraplength=400)
		setup_text.pack(anchor="w", padx=10)

		# How to Play
		ttk.Label(mainFrame, text="KĀ SPĒLĒT", font=("Helvetica", 12, "bold")).pack(anchor="w", pady=(15, 5))
		play_text = ttk.Label(mainFrame, text="• Spēlētāji pēc kārtas dala pašreizējo skaitli ar 2 vai 3\n• Skaitlis jāiedala bez atlikuma\n• Spēle beidzas, kad skaitlis vairs nedalās", justify=tk.LEFT, wraplength=400)
		play_text.pack(anchor="w", padx=10)

		# Scoring Rules
		ttk.Label(mainFrame, text="PUNKTU SADALE", font=("Helvetica", 12, "bold")).pack(anchor="w", pady=(15, 5))
		scoring_text = ttk.Label(mainFrame, text="• Pāra skaitlis → +1 punkts cilvēkam\n• Nepāra skaitlis → -1 punkts cilvēkam\n• Skaitlis beidzas ar 0 vai 5 → +1 punkts bankai", justify=tk.LEFT, wraplength=400)
		scoring_text.pack(anchor="w", padx=10)

		# Winning
		ttk.Label(mainFrame, text="SPĒLES BEIGAS", font=("Helvetica", 12, "bold")).pack(anchor="w", pady=(15, 5))
		winning_text = ttk.Label(mainFrame, text="• Pēdējais, kurš veica gājienu, iztukšo banku savā labā\n• Vairāk punktu beigās = Uzvarētājs", justify=tk.LEFT, wraplength=400)
		winning_text.pack(anchor="w", padx=10)

		# Back button
		backBtn = ttk.Button(self, text="ATPAKAĻ", command=lambda: app.show_page("MainMenuPage"))
		backBtn.pack(pady=20)