import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import ttk

class GamePage(tk.Frame):
	def __init__(self, parent, app):
		super().__init__(parent)

		# mainīgie, kam jāapdeitojas
		self.playerScore = tk.StringVar()
		self.bankScore = tk.StringVar()
		self.aiScore = tk.StringVar()
		self.currentTurn = tk.StringVar()

		self.aiThinking = False

		# punktu rāmis ar virsrakstu
		pointsFrame = tk.Frame(self, bd=0, highlightthickness=1, highlightbackground="gray")
		pointsFrame.place(relx=0.5, rely=0.1, anchor="center")
		pointsLabel = ttk.Label(pointsFrame, text="Punkti", font=("Verdana", 15, "bold"))
		pointsLabel.grid(row=0, column=2, pady=5)

		# punktu labels ar atdalītājiem
		self.createPointsLabel(pointsFrame, self.playerScore, ("Arial", 12), 1, 0, 40, 10)
		tk.Frame(pointsFrame, bg="white", width=1).grid(row=1, column=1, sticky="ns", pady=5)
		self.createPointsLabel(pointsFrame, self.bankScore, ("Arial", 12), 1, 2, 40, 10)
		tk.Frame(pointsFrame, bg="white", width=1).grid(row=1, column=3, sticky="ns", pady=5)
		self.createPointsLabel(pointsFrame, self.aiScore, ("Arial", 12), 1, 4, 40, 10)

		# šobrīdēji dalāmā skaitļa attēlojums
		currentNumberFrame = tk.Frame(self, bd=5, relief="raised")
		currentNumberFrame.place(relx=0.5, rely=0.3, anchor="center")
		self.currentNumber = tk.IntVar()
		currentNumberLabel = ttk.Label(
			currentNumberFrame,
			textvariable=self.currentNumber,
			font=("Arial", 40)
		)
		currentNumberLabel.pack(padx=50, pady=20)

		# šobrīdējā gājiena attēlojums
		turnLabel = ttk.Label(self, textvariable=self.currentTurn, font=("Arial", 12))
		turnLabel.place(relx=0.5, rely=0.43, anchor="center")

		# rāmis priekš dalīšanas pogām
		buttonFrame = tk.Frame(self, bd=0)
		buttonFrame.place(relx=0.5, rely=0.52, anchor="center")

		# pogas ar kurām dala
		self.divideBy2Result = tk.StringVar()
		divideBy2button = self.createFormattedButton(
			buttonFrame,
			"/ 2",
			self.divideBy2Result,
			command=lambda: self.divideByNumber(app, 2)
		)
		divideBy2button.grid(row=0, column=0, padx=40)

		self.divideBy3Result = tk.StringVar()
		divideBy3button = self.createFormattedButton(
			buttonFrame,
			"/ 3",
			self.divideBy3Result,
			command=lambda: self.divideByNumber(app, 3)
		)
		divideBy3button.grid(row=0, column=1, padx=40)

		# beigšanas poga
		backBtn = ttk.Button(self, text="BEIGT SPĒLI", command=lambda: app.show_page("MainMenuPage"))
		backBtn.place(relx=0.5, rely=0.9, anchor="center")
	
	
	def refresh(self, app):
		# updeito visus mainīgos, paņemot info no gamestate
		self.currentNumber.set(app.game.current_number)

		# punkti
		self.playerScore.set("Spēlētājs: " + str(app.game.player_score))
		self.bankScore.set("Banka: " + str(app.game.bank_score))
		self.aiScore.set("Dators: " + str(app.game.ai_score))

		# gājiens
		if app.game.turn == "cilvēks":
			self.currentTurn.set("Cilvēka gājiens")
		else: self.runTheAI(app)

		# dalījuma rezultāts
		self.divideBy2Result.set(self.createResultLabel(app, 2))
		self.divideBy3Result.set(self.createResultLabel(app, 3))
	
	def divideByNumber(self, app, number):
		# dalīšana
		if app.game.current_number % number != 0:
			msgbox.showwarning("Nepareiza dalīšana", "Dalot ar šo skaitli neveidojās vesels skaitlis, izvēlieties otru!")
			return
		app.game.divideByNumber(number)
		self.refresh(app)

	def runTheAI(self, app):
		# domāšanas animācija priekš AI
		self.aiThinking = True
		self.currentTurn.set("Dators domā")
		self.after(750, lambda: self.currentTurn.set("Dators domā."))
		self.after(1500, lambda: self.currentTurn.set("Dators domā.."))
		self.after(2250, lambda: self.currentTurn.set("Dators domā..."))
		self.after(3000, lambda: self.finishAITurn(app))

	def finishAITurn(self, app):
		app.game.runTheAI()
		self.aiThinking = False
		self.refresh(app)

	# uztaisa punktu tekstiņus īsākā veidā
	def createPointsLabel(self, parent, var, font, row, column, padx, pady):
		newLabel = ttk.Label(parent, textvariable=var, font=font)
		newLabel.grid(row=row, column=column, padx=padx, pady=pady)
	
	# uztaisa formatētu dalīšanas pogu (ar frame)
	def createFormattedButton(self, parent, operator, resultVar, command=None):
		buttonFrame = tk.Frame(parent, relief="raised", bd=2, cursor="hand2")
		
		operatorLabel = ttk.Label(buttonFrame, text=operator, font=("Arial", 16, "bold"))
		operatorLabel.pack(pady=5)
		
		resultLabel = ttk.Label(buttonFrame, textvariable=resultVar, font=("Arial", 12))
		resultLabel.pack(pady=5, padx=10)
		
		if command:
			buttonFrame.bind("<Button-1>", lambda e: command())
			operatorLabel.bind("<Button-1>", lambda e: command())
			resultLabel.bind("<Button-1>", lambda e: command())
		
		return buttonFrame
	
	# parāda dalījuma rezultātu uz pogas
	def createResultLabel(self, app, divider):
		cur = app.game.current_number
		result = int(app.game.current_number / divider)
		if cur % divider != 0:
			return "Nedalās!"
		else:
			return "= " + str(int(result))