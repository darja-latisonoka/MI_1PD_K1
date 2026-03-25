import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import ttk

import time

class GamePage(tk.Frame):
	def __init__(self, parent, app):
		super().__init__(parent)

		self.app = app

		# mainīgie, kam jāapdeitojas
		self.playerScoreText = tk.StringVar()
		self.bankScoreText = tk.StringVar()
		self.aiScoreText = tk.StringVar()
		self.currentTurnText = tk.StringVar()

		# punktu rāmis ar virsrakstu
		pointsFrame = tk.Frame(self, bd=0, highlightthickness=1, highlightbackground="gray")
		pointsFrame.place(relx=0.5, rely=0.1, anchor="center")
		pointsLabel = ttk.Label(pointsFrame, text="Punkti", font=("Verdana", 15, "bold"))
		pointsLabel.grid(row=0, column=2, pady=5)

		# punktu labels ar atdalītājiem
		self.createPointsLabel(pointsFrame, self.playerScoreText, ("Arial", 12), 1, 0, 40, 10)
		tk.Frame(pointsFrame, bg="white", width=1).grid(row=1, column=1, sticky="ns", pady=5)
		self.createPointsLabel(pointsFrame, self.bankScoreText, ("Arial", 12), 1, 2, 40, 10)
		tk.Frame(pointsFrame, bg="white", width=1).grid(row=1, column=3, sticky="ns", pady=5)
		self.createPointsLabel(pointsFrame, self.aiScoreText, ("Arial", 12), 1, 4, 40, 10)

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

		# rāmis priekš dalīšanas pogām un gājēja parādīšanas, ko vēlāk uztaisa iekš refresh
		self.interactionFrame = tk.Frame(self, bd=0)
		self.interactionFrame.place(relx=0.5, rely=0.52, anchor="center")

		# rāmis priekš spēles beigu info parādīšanas
		self.gameEndFrame = tk.Frame(self, bd=0)
		self.gameEndFrame.place(relx=0.5, rely=0.7, anchor="center")

		# beigšanas poga
		backBtn = ttk.Button(self, text="BEIGT SPĒLI", command=lambda: app.show_page("MainMenuPage"))
		backBtn.place(relx=0.5, rely=0.9, anchor="center")
	
	# updeito visus mainīgos, paņemot info no gamestate
	def refresh(self, app):
		# skatlis
		self.currentNumber.set(app.game.current_number)

		# punkti
		self.playerScoreText.set("Spēlētājs: " + str(app.game.player_score))
		self.bankScoreText.set("Banka: " + str(app.game.bank_score))
		self.aiScoreText.set("Dators: " + str(app.game.ai_score))

		# spēles beigas
		if app.game.game_has_ended:
			self.setupInteractionFrame(forHuman=False)
			self.showEndResults()
			return

		# iztīram beigu rāmi (priekš nākamās spēles)
		self.clearFrame(self.gameEndFrame)
		self.gameEndFrame.configure(
			bd=0,
			highlightthickness=0
		)

		# setapo spaidāmās pogas
		if app.game.turn == "cilvēks":
			self.setupInteractionFrame(forHuman=True)
		else:
			self.setupInteractionFrame(forHuman=False)
			self.runTheAI(app)
	
	def divideByNumber(self, app, number):
		# dalīšana
		if app.game.current_number % number != 0:
			msgbox.showwarning("Nepareiza dalīšana", "Dalot ar šo skaitli neveidojās vesels skaitlis, izvēlieties otru!")
			return
		app.game.divideByNumber(number)
		self.refresh(app)

	# domāšanas animācija priekš AI
	def runTheAI(self, app):
		self.after(300, lambda: self.currentTurnText.set("Dators domā."))
		self.after(600, lambda: self.currentTurnText.set("Dators domā.."))
		self.after(900, lambda: self.currentTurnText.set("Dators domā..."))
		self.after(1200, lambda: self.currentTurnText.set("Dators domā."))
		self.after(1500, lambda: self.currentTurnText.set("Dators domā.."))
		self.after(1800, lambda: self.finishAITurn(app))

	# actual funkcija, kas liek ai izdarīt gājienu
	def finishAITurn(self, app):
		ai_choice = app.game.runTheAI()
		if ai_choice == 2:
			self.currentTurnText.set("<---- Datora izvēle")
		else:
			self.currentTurnText.set("Datora izvēle ---->")
		self.after(1200, lambda: self.refresh(app))
	
	def setupInteractionFrame(self, forHuman: bool):
		# iznīcina iepriekšējās pogas
		self.clearFrame(self.interactionFrame)

		# mainīgie
		parent = self.interactionFrame
		if forHuman:
			tempTurnText = "<- Cilvēka gājiens ->"
		elif self.app.game.game_has_ended:
			tempTurnText = "Paldies, ka spēlēji :)"
		else:
			tempTurnText = "Dators domā"

		# dalīt ar 2 poga
		divideBy2button = self.createButtonForInteractionFrame(2, forHuman)
		divideBy2button.grid(row=0, column=0, padx=40)

		# parāda, kam gājiens
		parent.grid_columnconfigure(1, weight=1, minsize=260)
		turnLabelFrame = tk.Frame(parent, bd=0)
		turnLabelFrame.grid(row=0, column=1, sticky='nsew')
		self.currentTurnText.set(tempTurnText)
		turnLabel = ttk.Label(
			turnLabelFrame, textvariable=self.currentTurnText,
			font=("Arial", 14),
			justify="center", anchor="center", width=30)
		turnLabel.pack(anchor="center")
		
		# dalīt ar 3 poga
		divideBy3button = self.createButtonForInteractionFrame(3, forHuman)
		divideBy3button.grid(row=0, column=2, padx=40)

	# uztaisa formatētu dalīšanas pogu (ar frame) (self, num, forHuman)
	def createButtonForInteractionFrame(self, num: int, forHuman: bool):

		# mainīgie
		parent = self.interactionFrame
		operator = "/ " + str(int(num))
		if self.app.game.current_number % num == 0:
			divResult = "= " + str(self.app.game.current_number // num)
		else: divResult = "Nedalās!"
		
		# ja priekš cilvēka, tad pogas ir clickable
		if forHuman:
			buttonFrame = tk.Frame(parent, relief="raised", bd=8, cursor="hand2")
			command = lambda: self.divideByNumber(self.app, num)
		else:
			buttonFrame = tk.Frame(parent, relief="raised", bd=8)
			command = None

		# uzliek to dalītāju uz pogas
		operatorLabel = ttk.Label(buttonFrame, text=operator, font=("Arial", 18, "bold"))
		operatorLabel.pack(pady=5)

		# uzliek rezultātu, kāds būs dalot, uz pogas
		resultLabel = ttk.Label(buttonFrame, text=divResult, font=("Arial", 14))
		resultLabel.pack(pady=5, padx=10)

		# pieliek funkciju pogai, ja tā domāta cilvēkam
		if command:
			buttonFrame.bind("<Button-1>", lambda e: command())
			operatorLabel.bind("<Button-1>", lambda e: command())
			resultLabel.bind("<Button-1>", lambda e: command())

		return buttonFrame
	
	# uztaisa punktu tekstiņus īsākā veidā
	def createPointsLabel(self, parent, var, font, row, column, padx, pady):
		newLabel = ttk.Label(parent, textvariable=var, font=font)
		newLabel.grid(row=row, column=column, padx=padx, pady=pady)

	# iznīcina visus objektus iekš kāda frame
	def clearFrame(self, frame):
		for child in frame.winfo_children():
			child.destroy()
	
	# parāda beigu rezultātus
	def showEndResults(self):
		parent = self.gameEndFrame
		self.clearFrame(parent)

		parent.configure(
			bd=3,
			relief="solid",
			highlightthickness=1,
			highlightbackground="#18cc00"
		)

		# parāda beigu virsrakstu
		gameEndText = "SPĒLES BEIGAS"
		gameEndLabel = ttk.Label(parent, text=gameEndText, font=("Arial", 22, "bold"))
		gameEndLabel.pack(pady=5)

		# parāda spēles uzvarētāju
		if self.app.game.player_score > self.app.game.ai_score:
			winner = "Cilvēks"
		elif self.app.game.ai_score > self.app.game.player_score:
			winner = "AI"
		else:
			winner = "Neizšķirts"
		gameEndResultText = "Uzvarētājs: " + winner
		gameEndResult = ttk.Label(parent, text=gameEndResultText, font=("Arial", 18))
		gameEndResult.pack(pady=5)
