from dummyCreature import *

class Tarrasque (creature):
	def __init__(self):
		self.name = "Tarrasque"
		self.armor_cls = 25
		self.hit_pts = 676
		self.curr_hp = self.hit_pts
		self.challnge_rtg = 30
		self.prof_bns = 9
		self.is_defeated = False

		self.strength = 30
		self.dexterity = 11
		self.constitution = 30
		self.intelligence = 3
		self.wisdom = 11
		self.charisma = 11

		self.dex_bns = 0
		self.atk_bns = 19

		def attack():
			totalDmg = multiattack()

			return totalDmg

		def multiattack():
			dmg = bite() + claw() + claw() + horn() + tail()

			return dmg

		def bite():
			#checks if attack hits
			self.attack_roll()

			dmgRoll = 0

			#if hits, rolls 4d12 + 10
			for i in range(4):
				dmgRoll = dmgRoll + random.randint(1,12)

			dmgRoll = dmgRoll + 10

			return dmgRoll

		def claw():
			#checks if attack hits
			self.attack_roll()

			dmgRoll = 0

			#if hits, rolls 4d8 + 10
			for i in range(4):
				dmgRoll = dmgRoll + random.randint(1,8)

			dmgRoll = dmgRoll + 10

			return dmgRoll

		def horn():
			#checks if attack hits
			self.attack_roll()

			dmgRoll = 0

			#if hits, rolls 4d10 + 10
			for i in range(4):
				dmgRoll = dmgRoll + random.randint(1,10)

			dmgRoll = dmgRoll + 10

			return dmgRoll

		def tail():
			#checks if attack hits
			self.attack_roll()

			dmgRoll = 0

			#if hits, rolls 4d6 + 10
			for i in range(4):
				dmgRoll = dmgRoll + random.randint(1,6)

			dmgRoll = dmgRoll + 10

			return dmgRoll