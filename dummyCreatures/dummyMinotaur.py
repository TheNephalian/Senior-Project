from dummyCreature import *

class minotaur (creature):
	def __init__(self):
		minotaur.__init__

		self.armor_cls = 14
		self.hit_pts = 76
		self.curr_hp = self.hit_pts
		self.challnge_rtg = 3
		self.prof_bns = 2
		self.is_defeated = False

		self.strength = 18
		self.dexterity = 11
		self.constitution = 16
		self.intelligence = 6
		self.wisdom = 16
		self.charisma = 19

		self.dex_bns = 0
		self.atk_bns = 6

		def attack():
			totalDmg = gore()

			return totalDmg

		def gore():
			#checks if attack hits
			self.attack_roll()

			dmgRoll = 0

			#if hits, rolls 4d8 + 4
			for i in range(4):
				dmgRoll = dmgRoll + random.randint(1,8)

			dmgRoll = dmgRoll + 4

			return dmgRoll