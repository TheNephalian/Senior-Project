from dummyCreature import *

class Behir (creature):
	def __init__(self):
		self.name = "Behir"
		self.armor_cls = 17
		self.hit_pts = 168
		self.curr_hp = self.hit_pts
		self.challnge_rtg = 11
		self.prof_bns = 4
		self.is_defeated = False

		self.strength = 23
		self.dexterity = 16
		self.constitution = 18
		self.intelligence = 7
		self.wisdom = 14
		self.charisma = 11

		self.dex_bns = 3
		self.atk_bns = 10
		
		self.lbRecharge = True

		def attack():
			totalDmg = lightningBreath() + multiAttack()

			return totalDmg

		def multiAttack():
			dmg = bite() + constrict()

			return dmg

		def bite():
			#checks if attack hits
			self.attack_roll()

			dmgRoll = 0

			#if hits, rolls 3d10 + 6
			for i in range(3):
				dmgRoll = dmgRoll + random.randint(1,10)

			dmgRoll = dmgRoll + 6

			return dmgRoll

		def constrict():
			#checks if attack hits
			self.attack_roll()

			dmgRoll = 0

			#if hits, rolls 4d10 + 12
			for i in range(4):
				dmgRoll = dmgRoll + random.randint(1,10)

			dmgRoll = dmgRoll + 12

			return dmgRoll

		def lightningBreath():
			#checks if lightning breath is recharged
			if (self.lbRecharge == False):
				rechargeRoll = random.randint(1,6)
				if (rechargeRoll == 5 | rechargeRoll == 6):
					self.lbRecharge = True

			#picks up to 2 players to deal damage to
			'''
			WIP
			'''
			dmgRoll = 0

			#rolls 12d10
			if (self.lbRecharge == True):
				for i in range(12):
					dmgRoll = dmgRoll + random.randint(1,10)

				self.lbRecharge = False

			return dmgRoll