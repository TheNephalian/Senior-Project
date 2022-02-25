from dummyCreature import *

class orc (creature):
	def __init__(self):
		orc.__init__

		self.armor_cls = 13
		self.hit_pts = 15
		self.curr_hp = self.hit_pts
		self.challnge_rtg = 1/2
		self.prof_bns = 2
		self.is_defeated = False

		self.strength = 16
		self.dexterity = 12
		self.constitution = 16
		self.intelligence = 7
		self.wisdom = 11
		self.charisma = 10

		self.dex_bns = 1
		self.atk_bns = 5

		def attack():
			totalDmg = greataxe()

			return totalDmg

		def greataxe():
			#checks if attack hits
			self.attack_roll

			dmgRoll = 0

			#if hits, rolls 1d12 + 3
			dmgRoll = dmgRoll + random.randint(1,12)
			
			dmgRoll = dmgRoll + 3

			return dmgRoll