import random
from tkinter import E
from dummyCreature import creature
from dummyCreatures import dummyCyclops, dummyMinotaur, dummyBugBear, dummyOrc, dummyZombie, dummyGiantRat
from player import *
from dummyPlayers import dummyFighter, dummyRanger, dummyRogue, dummyWizard

class combatSimulation():
	def __init__(self, creature, player_array):
		#the creature that's in combat
		self.creature = creature

		#self.creature = dummyGiantRat.GiantRat()
		#self.creature = dummyZombie.Zombie()
		#self.creature = dummyOrc.Orc()
		#self.creature = dummyBugBear.BugBear()
		#self.creature = dummyMinotaur.Minotaur()
		#self.creature = dummyCyclops.Cyclops()

		self.players = [] #array that holds the players (up to 4) that are in combat
		
		self.initiativeOrder = [] #keeps track of initiative (turn order)

		self.round = 0 #int that keeps track of the number of rounds that have passed in combat

		self.repeat_combat = True #boolean that will dicate whether combat continues or not.

		for i in range(0, len(player_array)):
			self.players.append(player_array[i])

	'''
	def __init__(self, creature):
		#the creature that's in combat
		self.creature = creature

		#self.creature = dummyGiantRat.GiantRat()
		#self.creature = dummyZombie.Zombie()
		#self.creature = dummyOrc.Orc()
		#self.creature = dummyBugBear.BugBear()
		#self.creature = dummyMinotaur.Minotaur()
		#self.creature = dummyCyclops.Cyclops()

		self.players = [] #array that holds the players (up to 4) that are in combat
		
		self.initiativeOrder = [] #keeps track of initiative (turn order)

		self.round = 0 #int that keeps track of the number of rounds that have passed in combat

		self.repeat_combat = True #boolean that will dicate whether combat continues or not.
		
		#This section will grab the chosen players from the user's input
		#For now, we'll hard code some players

		p1 = dummyFighter.Fighter()
		p1.lvl_change(1)

		p2 = dummyRanger.Ranger()
		p2.lvl_change(1)

		p3 = dummyRogue.Rogue()
		p3.lvl_change(1)

		p4 = dummyWizard.Wizard()
		p4.lvl_change(1)

		self.players.append(p1)
		self.players.append(p2)
		self.players.append(p3)
		self.players.append(p4)
		
		#This section will grab the chosen monster or load a custom moster
		#For now, we'll hard code a monster
	'''

	'''
	Helper function for initiative order.
	'''
	def partition(self, arr, low, high):
		i = (low - 1)
		pivot = arr[high]

		for j in range(low, high):
			if arr[j].initiative <= pivot.initiative:
				i = i + 1
				arr[i], arr[j] = arr[j], arr[i]
		
		arr[i + 1], arr[high] = arr[high], arr[i + 1]

		return (i + 1)

	'''
	Helper function for initiative order.
	'''
	def quickSort(self, arr, low, high):
		if len(arr) == 1:
			return arr

		if low < high:
			pi = self.partition(arr, low, high)

			self.quickSort(arr, low, pi - 1)
			self.quickSort(arr, pi + 1, high)

	'''
	Function that rolls initative for all combatanants
	'''
	def rollInit(self):
		#First, determines number of players and rolls their initiatives
		numPlayers = len(self.players)

		#Player initiatives
		if (numPlayers == 4):
			#print("4 players rolling initiative...")

			p1_init = self.players[0].roll_init()
			self.players[0].initiative = p1_init
			#print("The", self.players[0].name, "got a", p1_init)

			p2_init = self.players[1].roll_init()
			self.players[1].initiative = p2_init
			#print("The", self.players[1].name, "got a", p2_init)

			p3_init = self.players[2].roll_init()
			self.players[2].initiative = p3_init
			#print("The", self.players[2].name, "got a", p3_init)

			p4_init = self.players[3].roll_init()
			self.players[3].initiative = p4_init
			#print("The", self.players[3].name, "got a", p4_init)

			self.initiativeOrder.append(self.players[0])
			self.initiativeOrder.append(self.players[1])
			self.initiativeOrder.append(self.players[2])
			self.initiativeOrder.append(self.players[3])

		elif (numPlayers == 3):
			#print("3 players rolling intiative...")

			p1_init = self.players[0].roll_init()
			self.players[0].initiative = p1_init
			#print("The", self.players[0].name, "got a", p1_init)

			p2_init = self.players[1].roll_init()
			self.players[1].initiative = p2_init
			#print("The", self.players[1].name, "got a", p2_init)

			p3_init = self.players[2].roll_init()
			self.players[2].initiative = p3_init
			#print("The", self.players[2].name, "got a", p3_init)

			self.initiativeOrder.append(self.players[0])
			self.initiativeOrder.append(self.players[1])
			self.initiativeOrder.append(self.players[2])

		elif (numPlayers == 2):
			#print("2 players rolling intitiative...")

			p1_init = self.players[0].roll_init()
			self.players[0].initiative = p1_init
			#print("The", self.players[0].name, "got a", p1_init)

			p2_init = self.players[1].roll_init()
			self.players[1].initiative = p2_init
			#print("The", self.players[1].name, "got a", p2_init)

			self.initiativeOrder.append(self.players[0])
			self.initiativeOrder.append(self.players[1])

		elif (numPlayers == 1):
			#print("1 player rolling initiative...")

			p1_init = self.players[0].roll_init()
			self.players[0].initiative = p1_init
			#print("The", self.players[0].name, "got a", p1_init)

			self.initiativeOrder.append(self.players[0])

		else:
			print("No players detected. Ending simulation.")
			return

		#Creature initiative
		#print(self.creature.name, "rolling initiative...")
		#print()

		creature_init = self.creature.roll_init()
		#print("The", self.creature.name, "got a", creature_init)
		self.creature.initiative = creature_init

		self.initiativeOrder.append(self.creature)

		self.quickSort(self.initiativeOrder, 0, len(self.initiativeOrder) - 1)

		self.initiativeOrder.reverse()
		
		#print("**Initiative Order**")
		#for k in range (0, len(self.initiativeOrder)):
			#print(self.initiativeOrder[k].name, self.initiativeOrder[k].initiative)

		#print()

	def remove_from_combat(self):
		if (self.creature.is_defeated == True):
			self.repeat_combat = False

			return 

		for m in range (0, len(self.players)):
			if (m == len(self.players)):
				m = m - 1

			if (self.players[m].is_defeated == True):
				player_to_be_removed = self.players[m]

				#print(player_to_be_removed.name, "is defeated and must be removed from combat.")

				self.players.remove(player_to_be_removed)
				self.initiativeOrder.remove(player_to_be_removed)

				#print(player_to_be_removed.name, "has been removed from combat.")
				#print()

				#print("**New Initiative Order**")
				#for k in range (0, len(self.initiativeOrder)):
					#print(self.initiativeOrder[k].name, self.initiativeOrder[k].initiative)

				#print()
			if (len(self.players) == 0):
				#print("All players have been defeated!")
				#print()

				self.repeat_combat = False

				return

	def combatSim(self):
		#print("******")
		#print("Running combat simulation...")

		#print("Rolling initiative for all combatanants!")

		self.rollInit()

		#print("Combat Log:")

		while (self.repeat_combat == True):
			
			self.round = self.round + 1

			#print("Round:", self.round)
			for i in range (0, len(self.initiativeOrder)):
				self.initiativeOrder[i].has_not_attacked()

			#print("about to start new round")
			beforecombatLength = len(self.initiativeOrder)
			for l in range (0, len(self.initiativeOrder)):
				if (l >= len(self.initiativeOrder)):
					#print("in initiativeOrder arry: ", l)
     
					l = l - 1
    
				if(self.initiativeOrder[l-1].has_attacked() == False and l == len(self.initiativeOrder)-1):
					#print("cant skip any")
					l = l - 1
				elif(self.initiativeOrder[l-1].has_attacked() == False and beforecombatLength != len(self.initiativeOrder)):
					#print("can't skip any condition 2")
					l = l - 1

				if (self.repeat_combat == False):
					#print("can't repeat combat")
					break

				if(self.initiativeOrder[l].has_attacked() == False):
					...
					#print("\n****this means they have not attacked and before combat")
				elif(self.initiativeOrder[l].has_attacked() == True):
					#print("\n****this means player/creature has attacked and before combat")
					break

				self.initiativeOrder[l].attack(self)
		
				#if(self.initiativeOrder[l].has_attacked() == True):
					#print("this means player/creature has attacked and after combat****")
					#...
				#elif(self.initiativeOrder[l].has_attacked() == False):
					#print("this means they have not attacked and after combat****")
					#...
    
				if (self.remove_from_combat() == True):
					if (l == len(self.initiativeOrder)-1):
						#print("removed from combat and l == len")
						break
				
  
				if (self.repeat_combat == False):
					#print("\nbreak here cause combat is over\n")
					break

			#if (self.repeat_combat == False):
				#print("in array: ", len(self.initiativeOrder))
				#print("End of combat simulation.")
				#print()

		if(self.creature.is_defeated == True):
			#print(self.creature.name, "was defeated!")
			return 1
		else:
			#print(self.creature.name, "defeated all players!")
			return 0