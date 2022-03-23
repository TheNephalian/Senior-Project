import random
from tkinter import E
from dummyCreatures import dummyZombie
from player import *
from dummyPlayers import dummyFighter, dummyRanger, dummyRogue, dummyWizard

class combatSimulation():
	def __init__(self):
		self.creature = dummyZombie.Zombie() #the creature that's in combat

		self.players = [] #array that holds the players (up to 4) that are in combat
		
		'''
		This section will grab the chosen players from the user's input
		For now, we'll hard code some players
		'''
		p1 = dummyFighter.Fighter()
		p1.lvl_change(1)

		p2 = dummyRanger.Ranger()
		p2.lvl_change(1)

		p3 = dummyRogue.Rogue()
		p3.lvl_change(1)

		p4 = dummyWizard.Wizard()

		self.players.append(p1)
		self.players.append(p2)
		#self.players.append(p3)
		#self.players.append(p4)

		'''
		This section will grab the chosen monster or load a custom moster
		For now, we'll hard code a monster
		'''

		self.initiativeOrder = [] #keeps track of initiative (turn order)

	def partition(self, arr, low, high):
		i = (low - 1)
		pivot = arr[high]

		for j in range(low, high):
			if arr[j].initiative <= pivot.initiative:
				i = i + 1
				arr[i], arr[j] = arr[j], arr[i]
		
		arr[i + 1], arr[high] = arr[high], arr[i + 1]

		return (i + 1)

	def quickSort(self, arr, low, high):
		if len(arr) == 1:
			return arr

		if low < high:
			pi = self.partition(arr, low, high)

			self.quickSort(arr, low, pi - 1)
			self.quickSort(arr, pi + 1, high)

	def rollInit(self):
		numPlayers = len(self.players)

		#Player initiatives
		if (numPlayers == 4):
			print("4 players rolling initiative...")

			p1_init = self.players[0].roll_init()
			self.players[0].initiative = p1_init
			print("The", self.players[0].name, "got a", p1_init)

			p2_init = self.players[1].roll_init()
			self.players[1].initiative = p2_init
			print("The", self.players[1].name, "got a", p2_init)

			p3_init = self.players[2].roll_init()
			self.players[2].initiative = p3_init
			print("The", self.players[2].name, "got a", p3_init)

			p4_init = self.players[3].roll_init()
			self.players[3].initiative = p4_init
			print("The", self.players[3].name, "got a", p4_init)

			self.initiativeOrder.append(self.players[0])
			self.initiativeOrder.append(self.players[1])
			self.initiativeOrder.append(self.players[2])
			self.initiativeOrder.append(self.players[3])

		elif (numPlayers == 3):
			print("3 players rolling intiative...")

			p1_init = self.players[0].roll_init()
			self.players[0].initiative = p1_init
			print("The", self.players[0].name, "got a", p1_init)

			p2_init = self.players[1].roll_init()
			self.players[1].initiative = p2_init
			print("The", self.players[1].name, "got a", p2_init)

			p3_init = self.players[2].roll_init()
			self.players[2].initiative = p3_init
			print("The", self.players[2].name, "got a", p3_init)

			self.initiativeOrder.append(self.players[0])
			self.initiativeOrder.append(self.players[1])
			self.initiativeOrder.append(self.players[2])

		elif (numPlayers == 2):
			print("2 players rolling intitiative...")

			p1_init = self.players[0].roll_init()
			self.players[0].initiative = p1_init
			print("The", self.players[0].name, "got a", p1_init)

			p2_init = self.players[1].roll_init()
			self.players[1].initiative = p2_init
			print("The", self.players[1].name, "got a", p2_init)

			self.initiativeOrder.append(self.players[0])
			self.initiativeOrder.append(self.players[1])

		elif (numPlayers == 1):
			print("1 player rolling initiative...")

			p1_init = self.players[0].roll_init()
			self.players[0].initiative = p1_init
			print("The", self.players[0].name, "got a", p1_init)

			self.initiativeOrder.append(self.players[0])

		else:
			print("No players detected. Ending simulation.")
			return

		#Creature initiative
		creature_init = self.creature.roll_init()
		print("The", self.creature.name, "got a", creature_init)
		self.creature.initiative = creature_init

		self.initiativeOrder.append(self.creature)

		self.quickSort(self.initiativeOrder, 0, len(self.initiativeOrder) - 1)

		self.initiativeOrder.reverse()
		
		print("**Initiative Order**")
		for k in range (0, len(self.initiativeOrder)):
			print(self.initiativeOrder[k].name, self.initiativeOrder[k].initiative)

		return
		
	def does_it_Hit(self):
		
		return

	#COMBAT IS WIP
	def combatSim(self):
		print("Rolling initiative for all combatanants!")

		self.rollInit()

		#for l in range (0, len(self.initiativeOrder)):
		#	self.initiativeOrder[l].attack()

		return