from dummyCreature import *

class PurpleWorm (creature):
	def __init__(self):
		self.name = "Purple Worm"
		self.armor_cls = 18
		self.hit_pts = 247
		self.curr_hp = self.hit_pts
		self.challnge_rtg = 15
		self.prof_bns = 5
		self.is_defeated = False

		self.strength = 28
		self.dexterity = 7
		self.constitution = 22
		self.intelligence = 1
		self.wisdom = 8
		self.charisma = 4

		self.dex_bns = -2
		self.atk_bns = 14

		def attack():
			totalDmg = multiattack()

			return totalDmg

		def multiattack():
			dmg = bite() + tailStinger()

			return dmg

		def bite():
			#checks if attack hits
			self.attack_roll()

			dmgRoll = 0

			#if hits, rolls 3d8 + 9
			for i in range(3):
				dmgRoll = dmgRoll + random.randint(1,8)

			dmgRoll = dmgRoll + 9

			return dmgRoll

		def tailStinger():
			#checks if attack hits
			self.attack_roll

			dmgRoll = 0

			#if hits, rolls 15d6 + 9
			for i in range(15):
				dmgRoll = dmgRoll + random.randint(1,6)

			dmgRoll = dmgRoll + 9

			return dmgRoll