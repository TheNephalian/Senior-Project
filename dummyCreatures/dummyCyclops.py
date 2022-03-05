from dummyCreature import *

class Cyclops (creature):
	def __init__(self):
		self.name = "Cyclops"
		self.armor_cls = 14
		self.hit_pts = 138
		self.curr_hp = self.hit_pts
		self.challnge_rtg = 6
		self.prof_bns = 3
		self.is_defeated = False

		self.strength = 22
		self.dexterity = 11
		self.constitution = 20
		self.intelligence = 8
		self.wisdom = 6
		self.charisma = 10

		self.dex_bns = 0
		self.atk_bns = 9

		def attack():
			totalDamage = multiattack()

			return totalDamage

		def multiattack():
			dmg = greatclub() + greatclub()

			return dmg

		def greatclub():
			#checks if attack hits
			self.attack_roll()

			dmgRoll = 0

			#if hits, rolls 3d8 + 6
			for i in range(3):
				dmgRoll = dmgRoll + random.randint(1,8)

			dmgRoll = dmgRoll + 6

			return dmgRoll