from dummyCreature import *
class ancientRedDragon (creature):
	def __init__(self):
		ancientRedDragon.__init__

		self.armor_cls = 22
		self.hit_pts = 546
		self.curr_hp = self.hit_pts
		self.challnge_rtg = 24
		self.prof_bns = 7
		self.is_defeated = False

		self.strength = 30
		self.dexterity = 10
		self.constitution = 29
		self.intelligence = 18
		self.wisdom = 15
		self.charisma = 23

		self.dex_bns = 0
		self.atk_bns = 17

		self.fbRecharge = True

		def attack():
			totalDmg = fireBreath() + multiAttack()

			return totalDmg

		def multiAttack():
			dmg = bite() + claw() + claw()

			return dmg

		def bite():
			#checks if attack hits
			self.attack_roll()

			dmgRoll = 0

			#if hits, rolls 2d10 + 10
			for i in range(2):
				dmgRoll = dmgRoll + random.randint(1,10)

			dmgRoll = dmgRoll + 10

			return dmgRoll

		def claw():
			#checks if attack hits
			self.attack_roll()

			dmgRoll = 0

			#if hits, rolls 2d6 + 10
			for i in range(2):
				dmgRoll = dmgRoll + random.randint(1,6)

			dmgRoll = dmgRoll + 10
			return dmgRoll

		def fireBreath():
			#checks if fire breath is recharged
			if (self.fbRecharge == False):
				rechargeRoll = random.randint(1,6)
				if (rechargeRoll == 5 | rechargeRoll == 6):
					self.fbRecharge = True

			#picks up to two players to deal damage to
			'''
			WIP
			'''
			dmgRoll = 0

			#rolls 26d6
			if (self.fbRecharge == True):
				for i in range(26):
					dmgRoll = dmgRoll + random.randint(1,6)

				self.fbRecharge = False

			return dmgRoll